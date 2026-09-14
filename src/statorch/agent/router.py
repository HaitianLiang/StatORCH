from __future__ import annotations
from dataclasses import dataclass
import numpy as np
import yaml
from pathlib import Path

@dataclass
class StageRule:
    fallback: str
    feature_index: int
    threshold: float
    action: str
    safe_threshold: float

class SavedArtifactRouter:
    """Replays saved one-feature HealthRule / safe thresholds on a supplied state vector.

    This class does not reconstruct an unavailable learned-router architecture.
    """
    def __init__(self, rules: dict[str,StageRule]): self.rules=rules
    @classmethod
    def from_yaml(cls,path):
        raw=yaml.safe_load(Path(path).read_text()); rules={}
        for stage,c in raw.items():
            hr=c['health_rule']; rules[stage]=StageRule(c['fallback'],int(hr['feature_index']),float(hr['threshold']),hr['action'],float(c['safe_threshold']))
        return cls(rules)
    def health_rule(self,stage,features):
        r=self.rules[stage]; return r.action if features[r.feature_index]>=r.threshold else r.fallback
    def safe_select(self,stage,features,predicted_gain):
        r=self.rules[stage]; proposed=self.health_rule(stage,features)
        if proposed==r.fallback: return r.fallback
        return proposed if predicted_gain>=r.safe_threshold else r.fallback

class DemoDiagnosisRouter:
    def choose_bundle(self, bundle_stats, costs):
        # bundle_stats[name] = {'domain_auc':..., 'unc_width':..., 'fit_score':...}
        scores={}
        for name,s in bundle_stats.items():
            health=max(1.0-2*abs(s['domain_auc']-0.5),0.05)
            scores[name]=(s['unc_width']+0.05)*health*(0.5+s['fit_score'])/max(costs[name],1e-9)
        return max(scores,key=scores.get),scores
