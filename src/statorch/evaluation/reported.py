from pathlib import Path
import pandas as pd

def load_reported(root='results/reported'):
    root=Path(root)
    return {p.stem: pd.read_csv(p) for p in root.glob('*.csv')}
