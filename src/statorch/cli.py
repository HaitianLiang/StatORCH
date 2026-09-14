from __future__ import annotations
import argparse, json
from pathlib import Path
from statorch.evaluation.demo_benchmark import run_demo
from statorch.reporting.frontend_export import export

def validate(root='.'):
    root=Path(root)
    required=['README.md','src/statorch/agent/state.py','results/reported/overall.csv','frontend/index.html']
    missing=[x for x in required if not (root/x).exists()]
    if missing: raise SystemExit('Missing required files: '+', '.join(missing))
    rows=(root/'results/reported/overall.csv').read_text().splitlines()
    if not any('StatOrch' in x for x in rows): raise SystemExit('Reported snapshot missing StatOrch row')
    print('Repository validation: OK')

def main():
    p=argparse.ArgumentParser(prog='statorch'); sub=p.add_subparsers(dest='cmd',required=True)
    d=sub.add_parser('demo'); d.add_argument('--config',default='configs/demo.yaml'); d.add_argument('--out',default='results/demo')
    v=sub.add_parser('validate'); v.add_argument('--root',default='.')
    e=sub.add_parser('export-frontend'); e.add_argument('--reported',default='results/reported'); e.add_argument('--frontend',default='frontend/data')
    a=p.parse_args()
    if a.cmd=='demo': print(json.dumps(run_demo(a.config,a.out),indent=2))
    elif a.cmd=='validate': validate(a.root)
    else: export(a.reported,a.frontend); print('Frontend data exported.')
