from dataclasses import dataclass

@dataclass(frozen=True)
class ExternalProtocol:
    dataset: str
    source: str
    calibration: str
    targets: tuple[str,...]
    budgets: tuple[int,...]

REALDISP=ExternalProtocol('REALDISP','train-subject ideal','train-subject self-placement',('held-out self-placement','held-out induced displacement'),(1,3,5,9))
GAS_DRIFT=ExternalProtocol('Gas Sensor Array Drift','B1-B3','B4-B6',('B7','B8','B9','B10'),(2,4,8,16))
