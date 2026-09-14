from statorch.agent.router import SavedArtifactRouter

def test_saved_router_loads():
    r=SavedArtifactRouter.from_yaml('configs/router_artifacts.yaml')
    f=[0.0]*20; f[16]=.1
    assert r.health_rule('quantification',f)=='BBSE'
    assert r.safe_select('quantification',f,.01)=='EMQ'
    assert r.safe_select('quantification',f,.08)=='BBSE'
