from pathlib import Path
import json, csv

def _csv_records(path):
    with open(path,encoding='utf-8') as f: return list(csv.DictReader(f))

def export(reported='results/reported',frontend='frontend/data'):
    r=Path(reported); f=Path(frontend); f.mkdir(parents=True,exist_ok=True)
    mapping={'overall':'overall.csv','splits':'splits.csv','measurement_ablation':'measurement_ablation.csv','module_routing':'module_routing.csv','external':'external_summary.csv'}
    data={k:_csv_records(r/v) for k,v in mapping.items()}
    for k,v in data.items(): (f/f'{k}.json').write_text(json.dumps(v,indent=2),encoding='utf-8')
    for name in ['matched_openworld','router_artifacts','claim_scope','trajectory']:
        src=r/f'{name}.json'
        if src.exists(): (f/f'{name}.json').write_text(src.read_text(),encoding='utf-8')
    return data
