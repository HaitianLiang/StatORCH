# Data and evaluation protocol

## Controlled demo

The local demo creates a seeded multi-class, multi-sensor Gaussian source/target problem with:

- prior shift;
- sensor-specific conditional corruption;
- optional out-of-reference samples;
- explicit measurement bundles and costs.

Evaluator truth lives inside `HiddenTruth` and is not exposed to the controller.

## External protocols represented in config

### REALDISP

- source: training-subject ideal placement;
- calibration: training-subject self-placement;
- moderate target: held-out self-placement;
- severe target: held-out induced displacement;
- budgets: 1, 3, 5, 9 sensors;
- target pilot is charged/excluded from evaluation episodes.

### Gas Sensor Array Drift

- source: B1–B3;
- calibration: B4–B6;
- targets: B7, B8, B9, B10;
- budgets: 2, 4, 8, 16 sensors.

The raw datasets are not redistributed.
