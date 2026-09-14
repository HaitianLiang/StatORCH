from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class ToolSpec:
    name: str
    family: str
    implementation: str = 'core'
    notes: str = ''

DEFAULT_REGISTRY = {
    'PCC': ToolSpec('PCC','quantification'),
    'EMQ': ToolSpec('EMQ','quantification'),
    'PACC': ToolSpec('PACC','quantification'),
    'BBSE': ToolSpec('BBSE','quantification'),
    'MAHALANOBIS': ToolSpec('MAHALANOBIS','ood'),
    'EATA': ToolSpec('EATA','adaptation','optional_adapter'),
    'TENT': ToolSpec('TENT','adaptation','optional_adapter'),
    'FWSP': ToolSpec('FWSP','acquisition','interface'),
}
