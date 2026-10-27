"""Condensed, generated push report. No new normative source, commits or publication.

ReportLab is optional for the core and pinned only for the PDF/CI adapter.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
from xml.sax.saxutils import escape

from .io import Invalid, loads
from . import release_docs as rd

REPOSITORY = 'https://github.com/Migueluckleo/CONTPAQi-DS-Specs-Driven-Design'
LABELS = {'added': 'Agregado', 'changed': 'Modificado', 'fixed': 'Corregido', 'removed': 'Eliminado'}


def collect(root, receipt, checks=None):
    checks = checks or {}
    passed = receipt.get('status') == 'PASS'
    if passed:
        expected = rd.verify(root, receipt['base'], receipt['head'])
        if any(receipt.get(k) != v for k, v in expected.items()):
            raise Invalid('PDF receipt does not match verified Git history')
        if receipt.get('tag'):
            rd.ci(root, {'ref': receipt['tag'], 'after': receipt['head']}, 'push')
    head = rd.commit(root, receipt['head'])
    base = receipt['base']
    ids = rd.commits(root, base, head)
    changes = rd.files(root, base, head)
    notes, components, pending, decisions, tests, subjects = [], [], [], set(), [], []
    if passed:
        for name in receipt['records']:
            record = rd.parse_record(rd.blob(root, head, name))
            notes.append(name)
            components += record['components']
            pending += record['pending']
            decisions.update(record['decisions'])
            tests += record['tests']
            subjects += record['commits']
    else:
        for oid in ids:
            subjects.append({'sha': oid, 'subject': rd.git(root, 'show', '-s', '--format=%s', oid).decode().strip(), 'category': 'changed'})
        pending.append('Incumplimiento: ' + receipt.get('reason', 'No se validó la documentación del envío.'))
    failed_checks = [k for k, v in checks.items() if v != 'success']
    if failed_checks:
        pending.append('Controles CI sin PASS: ' + ', '.join(failed_checks))
    groups = {key: [] for key in LABELS}
    seen = set()
    for item in subjects:
        if item['sha'] in seen:
            continue
        seen.add(item['sha'])
        groups[item['category']].append(item)
    unique_components = []
    for c in components:
        key = (c['id'], c['from']['version'] if c['from'] else None, c['to']['version'] if c['to'] else None)
        if key not in {(x['id'], x['from']['version'] if x['from'] else None, x['to']['version'] if x['to'] else None) for x in unique_components}:
            unique_components.append(c)
    return {'status': 'PASS' if passed and not failed_checks else 'NONCOMPLIANT', 'head': head, 'base': base,
            'commits': len(ids), 'files': len(changes), 'file_statuses': dict(Counter(c['status'] for c in changes)),
            'groups': groups, 'records': notes, 'components': unique_components, 'pending': list(dict.fromkeys(pending)),
            'decisions': sorted(decisions), 'tests': tests, 'checks': checks,
            'date': rd.git(root, 'show', '-s', '--format=%cI', head).decode().strip(),
            'run_id': receipt.get('run_id'), 'tag': receipt.get('tag'),
            'kind': 'release' if receipt.get('tag') else 'development'}


def render(report, output):
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='BHBody', fontName='Helvetica', fontSize=9.1, leading=13, textColor=colors.HexColor('#243650'), spaceAfter=5, splitLongWords=True))
    styles.add(ParagraphStyle(name='BHSmall', parent=styles['BHBody'], fontSize=7.6, leading=10.5))
    styles.add(ParagraphStyle(name='BHHeading', parent=styles['BHBody'], fontName='Helvetica-Bold', fontSize=11, leading=15, spaceBefore=10, spaceAfter=5))
    styles.add(ParagraphStyle(name='BHTitle', fontName='Helvetica-Bold', fontSize=24, leading=28, textColor=colors.HexColor('#123BA3'), spaceAfter=5))
    def clean(value):
        return str(value).replace('\u2011', '-').replace('\u2013', '-').replace('\u2014', '-').replace('\x00', '')
    def p(value, style='BHBody'):
        return Paragraph(escape(clean(value)), styles[style])
    def link(label, url):
        return Paragraph('<link href="'+escape(url, {'"': '&quot;'})+'" color="#1748BB">'+escape(clean(label))+'</link>', styles['BHSmall'])
    def short(value, size=230):
        value = clean(value)
        return value if len(value) <= size else value[:size-3]+'...'
    story = [p('BLUE HEART DS', 'BHSmall'), p('Release notes', 'BHTitle'),
             p('Resumen del envío | '+report['kind']+' | '+report['date'][:10], 'BHSmall'), Spacer(1, 5*mm)]
    state = 'VALIDACIÓN DOCUMENTAL: PASS' if report['status'] == 'PASS' else 'ENVÍO CON INCUMPLIMIENTO'
    bar = Table([[p(state), p(str(report['commits'])+' commits / '+str(report['files'])+' archivos')]], colWidths=[100*mm, 70*mm])
    bar.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#EAF0FF' if report['status']=='PASS' else '#FFF0E8')),('BOX',(0,0),(-1,-1),0.5,colors.HexColor('#BFCEFE')),('LEFTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    story += [bar, Spacer(1, 3*mm), link('Commit final: '+report['head'], REPOSITORY+'/commit/'+report['head'])]
    counts=report['file_statuses']
    story.append(p('Archivos: '+str(counts.get('A',0))+' altas, '+str(counts.get('M',0))+' modificaciones, '+str(counts.get('D',0))+' bajas. Los renombres se cuentan como baja y alta.', 'BHSmall'))
    for category, label in LABELS.items():
        rows = report['groups'][category]
        if not rows:
            continue
        section=[p(label,'BHHeading')]
        section += [p('- '+short(row['subject'])+' ['+row['sha'][:10]+']') for row in rows[:4]]
        if len(rows)>4:
            section.append(p(str(len(rows)-4)+' entradas adicionales en el registro MD.', 'BHSmall'))
        story += section
    story.append(p('Pruebas y verificaciones', 'BHHeading'))
    if report['checks']:
        story.append(p('CI: '+' | '.join(k+': '+('PASS' if v=='success' else v.upper()) for k,v in report['checks'].items())))
    latest = {}
    for t in report['tests']:
        label = 'Arquitectura' if t['command'][-1]=='check' else 'Infraestructura'
        m=re.search(r'Ran (\d+) tests?', t['output'])
        latest[label]=t['status']+(' ('+m[1]+' pruebas)' if m else '')
    if latest:
        story.append(p('Evidencia registrada: '+' | '.join(k+': '+v for k,v in latest.items())))
    story.append(p('Estos controles no acreditan QA visual de Figma, accesibilidad web ni aprobación independiente.', 'BHSmall'))
    if report['components']:
        story.append(p('Versiones de componentes', 'BHHeading'))
        for c in report['components'][:5]:
            before = c['from']['version'] if c['from'] else 'alta'
            after = c['to']['version'] if c['to'] else 'retirado'
            story.append(p(c['id']+': '+before+' -> '+after+' | '+c['impact']+' | '+short(c['reason'],150)))
        if len(report['components'])>5:
            story.append(p('Más componentes en el registro MD.','BHSmall'))
    else:
        story.append(p('Componentes: sin cambios registrados.' if report['status']=='PASS' else 'Componentes: no certificados por este envío.', 'BHSmall'))
    story.append(p('Pendientes y decisiones', 'BHHeading'))
    if report['pending']:
        for value in report['pending'][:5]:
            story.append(p('- '+short(value,260)))
        if len(report['pending'])>5:
            story.append(p(str(len(report['pending'])-5)+' pendientes adicionales en el registro MD.','BHSmall'))
    else:
        story.append(p('Sin pendientes declarados en las notas de este envío.'))
    if report['decisions']:
        story.append(p('Decisiones: '+', '.join(report['decisions']), 'BHSmall'))
    story.append(p('Registro verificable', 'BHHeading'))
    for note in report['records'][:4]:
        story.append(link('Nota MD: '+Path(note).name[:16]+'...', REPOSITORY+'/blob/'+report['head']+'/'+note))
    story.append(link('Historial completo del commit y sus archivos', REPOSITORY+'/commit/'+report['head']))
    if report['run_id']:
        story.append(link('Ejecución CI y artefactos', REPOSITORY+'/actions/runs/'+str(report['run_id'])))
    story.append(p('PDF derivado y condensado. El contrato BH-P08 y los registros MD conservan las reglas y el detalle completo. No constituye una release oficial salvo indicación y autorización explícitas.', 'BHSmall'))
    def footer(canvas, doc):
        canvas.setStrokeColor(colors.HexColor('#BFCEFE'));canvas.line(20*mm,17*mm,190*mm,17*mm)
        canvas.setFont('Helvetica',7);canvas.setFillColor(colors.HexColor('#586A84'))
        canvas.drawString(20*mm,12*mm,'Blue Heart DS | '+report['head'][:12])
        canvas.drawRightString(190*mm,12*mm,'Página '+str(doc.page))
    doc=SimpleDocTemplate(str(output),pagesize=(210*mm,297*mm),rightMargin=20*mm,leftMargin=20*mm,topMargin=18*mm,bottomMargin=23*mm,
                          title='Blue Heart DS - Release notes '+report['head'][:12],author='Blue Heart DS',pageCompression=1)
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    return output


def main():
    parser=argparse.ArgumentParser(description='BH-P08 | PDF condensado derivado del receipt del push')
    parser.add_argument('--root',type=Path,default=Path.cwd())
    parser.add_argument('--receipt',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--check',action='append',default=[],metavar='NAME:success|failure|skipped|cancelled')
    args=parser.parse_args()
    try:
        if not args.output.resolve().is_relative_to(args.root.resolve()) or args.output.resolve().is_relative_to((args.root/'output').resolve()):
            checks={}
            for value in args.check:
                name,status=value.split(':',1)
                if name in checks or status not in {'success','failure','skipped','cancelled'}:
                    raise Invalid('Invalid or duplicated CI check outcome')
                checks[name]=status
            report=collect(args.root,loads(args.receipt.read_bytes()),checks)
            output=render(report,args.output)
            print(json.dumps({'status':'CREATED','report_status':report['status'],'path':str(output),'head':report['head']},ensure_ascii=False))
            return 0
        raise Invalid('PDF must be generated outside tracked content (output/ or runner temp)')
    except (Invalid,OSError,KeyError,TypeError,ValueError,ImportError) as error:
        print(json.dumps({'status':'BLOCKED','reason':str(error)},ensure_ascii=False));return 2


if __name__=='__main__':
    raise SystemExit(main())
