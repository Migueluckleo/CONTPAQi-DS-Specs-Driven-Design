from pathlib import Path
import tempfile
import unittest
import importlib.util

from blueheart.io import Invalid
from blueheart import release_docs as rd
from blueheart import release_pdf as pdf


class ReleasePDFTests(unittest.TestCase):
    def setUp(self):
        from test_release_docs import ReleaseDocsTests
        self.fixture=ReleaseDocsTests();self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root=self.fixture.root

    def report(self):
        head,_=self.fixture.close()
        receipt=rd.verify(self.root,rd.EMPTY,head)
        return receipt,pdf.collect(self.root,receipt)

    def test_verified_report_cites_actual_head_counts_and_notes(self):
        receipt,report=self.report()
        self.assertEqual(report['status'],'PASS')
        self.assertEqual(report['head'],receipt['head'])
        self.assertEqual(report['commits'],2)
        self.assertEqual(report['records'],receipt['records'])
        self.assertEqual(len(report['groups']['added']),1)
        self.assertEqual(report['components'],[])

    def test_tampered_receipt_cannot_produce_a_pass_report(self):
        receipt,_=self.report()
        receipt['commits']=[]
        with self.assertRaisesRegex(Invalid,'receipt'):
            pdf.collect(self.root,receipt)

    def test_development_receipt_cannot_claim_an_official_release(self):
        receipt,_=self.report()
        receipt['tag']='refs/tags/v1.0.0'
        with self.assertRaises(Invalid):
            pdf.collect(self.root,receipt)

    def test_missing_documentation_produces_honest_failure_report(self):
        with self.assertRaises(Invalid):
            rd.verify(self.root,rd.EMPTY,self.fixture.initial)
        receipt=rd.failure_receipt(self.root,{'before':'0'*40,'after':self.fixture.initial},'push','Undocumented commits')
        report=pdf.collect(self.root,receipt,{'documentation':'failure'})
        self.assertEqual(report['status'],'NONCOMPLIANT')
        self.assertEqual(report['records'],[])
        self.assertIn('Incumplimiento: Undocumented commits',report['pending'])
        self.assertEqual(report['head'],self.fixture.initial)

    def test_successful_documentation_does_not_hide_failed_actual_ci_checks(self):
        receipt,_=self.report()
        report=pdf.collect(self.root,receipt,{'architecture':'success','tests':'failure','documentation':'success'})
        self.assertEqual(report['status'],'NONCOMPLIANT')
        self.assertTrue(any('tests' in p for p in report['pending']))

    def test_component_versions_and_pending_qa_are_preserved(self):
        self.fixture.component('2.0.0')
        self.fixture.save('feat: incorporar componente')
        record=self.fixture.note(pending=['Verificación independiente pendiente'])
        head,_=self.fixture.close(record)
        report=pdf.collect(self.root,rd.verify(self.root,rd.EMPTY,head))
        self.assertEqual(report['components'][0]['to']['version'],'2.0.0')
        self.assertIn('Verificación independiente pendiente',report['pending'])

    @unittest.skipUnless(importlib.util.find_spec('reportlab'),'Optional PDF adapter not installed in core interpreter')
    def test_pdf_render_handles_accents_and_markup_as_text(self):
        self.fixture.write('documento.txt','Cambios de diseño y función')
        self.fixture.save('fix: documentación <segura> & corrección de acentos')
        receipt,report=self.report()
        with tempfile.TemporaryDirectory() as temp:
            output=pdf.render(report,Path(temp)/'notes.pdf')
            self.assertTrue(output.read_bytes().startswith(b'%PDF-'))
            self.assertTrue(output.read_bytes().rstrip().endswith(b'%%EOF'))
            self.assertGreater(output.stat().st_size,2000)

    @unittest.skipUnless(importlib.util.find_spec('reportlab'),'Optional PDF adapter not installed in core interpreter')
    def test_pdf_failure_output_keeps_noncompliance(self):
        receipt=rd.failure_receipt(self.root,{'before':'0'*40,'after':self.fixture.initial},'push','Falta documentación')
        report=pdf.collect(self.root,receipt)
        with tempfile.TemporaryDirectory() as temp:
            output=pdf.render(report,Path(temp)/'failed.pdf')
            self.assertTrue(output.exists())
            self.assertEqual(report['status'],'NONCOMPLIANT')
