"""Reproduce la proyección vigente: baseline inmutable más reconciliación autorizada."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).parents[2]/"implementations/figma/tab-reconciliation-plan.py"),run_name="__main__")
