from statorch.evaluation.demo_benchmark import run_demo

def test_demo_smoke(tmp_path):
    r=run_demo('configs/demo.yaml',tmp_path)
    assert r['selected_bundle'] in {'S1','S3','S4','S13','ALL'}
    assert 0 <= r['selected_beta_l1'] <= 2
    assert (tmp_path/'certificate.json').exists()
