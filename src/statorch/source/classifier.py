from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from sklearn.linear_model import LogisticRegression

@dataclass
class SourceModel:
    model: LogisticRegression
    source_prior: np.ndarray
    classes_: np.ndarray

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        return self.model.predict_proba(x)


def train_source_classifier(x: np.ndarray, y: np.ndarray, seed: int = 0) -> SourceModel:
    model=LogisticRegression(max_iter=700, C=1.0, random_state=seed)
    model.fit(x,y)
    classes=model.classes_
    counts=np.array([(y==k).sum() for k in classes],float)
    prior=counts/counts.sum()
    return SourceModel(model, prior, classes)
