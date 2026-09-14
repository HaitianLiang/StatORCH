import pandas as pd

def test_reported_headline():
    df=pd.read_csv('results/reported/overall.csv'); s=df[df.method=='StatOrch'].iloc[0]
    assert abs(s.beta_l1-.224)<1e-12 and abs(s.macro_f1-.773)<1e-12 and int(s.cost)==802
