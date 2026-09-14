"""Print the structured reported-result snapshot.

This script intentionally does not claim to rerun unavailable raw experiments.
"""
import pandas as pd
from pathlib import Path
for p in sorted(Path('results/reported').glob('*.csv')):
    print('
##',p.name); print(pd.read_csv(p).to_string(index=False))
