# StatOrch

**Evidence-grounded statistical orchestration for inference under unknown distribution shift.**

StatOrch is a research codebase for closed-loop statistical inference on unlabeled target environments. Mature estimators and diagnostic tools produce typed numerical evidence; the controller admits only contract-valid actions, chooses an intervention, recomputes diagnostics after execution, and stores an auditable decision certificate.

> **Scope.** This repository contains an executable reference implementation of the documented StatOrch interfaces, a self-contained controlled demo, reported-result snapshots, tests, and a dependency-free web dashboard. It does **not** pretend to contain raw external datasets, unpublished checkpoints, or missing router-training artifacts that were not present in the supplied project materials.

## What is included

- Typed statistical state: prevalence, uncertainty, shift, fit/residual, representation health, open-world evidence, information value, cost, and tool health.
- Tool contracts and admissibility gating.
- Quantification: PCC, EMQ/SLD-style prior adjustment, PACC, BBSE.
- Statistical sensors: MMD, domain-classifier AUC, bootstrap prevalence bands, residual/fit diagnostics, estimator disagreement, tool health.
- OOD: Mahalanobis reference score.
- Acquisition policies: fixed, random, static ranking, myopic information/cost ranking, and a diagnosis-aware safe policy interface.
- Stage routers matching the saved fallback / HealthRule / Safe-threshold artifacts used by the latest manuscript.
- Decision certificates: evidence → diagnosis → action → pre/post diagnostic change.
- Controlled synthetic demo and smoke benchmark.
- Structured snapshots of the currently reported controlled, module-routing, and external results.
- A standalone frontend dashboard under `frontend/`.

## Repository layout

```text
StatORCH/
├── configs/                  # executable configs and saved router artifacts
├── docs/                     # architecture, protocols, claims
├── examples/                 # minimal API examples
├── frontend/                 # dependency-free interactive dashboard
├── scripts/                  # run / validate / export utilities
├── src/statorch/
│   ├── agent/                # state, contracts, routers, verifier, controller
│   ├── data/                 # synthetic data + episode structures
│   ├── evaluation/           # demo benchmark + reported snapshot loader
│   ├── metrics/              # prevalence / classification / OOD metrics
│   ├── reporting/            # JSON/HTML export helpers
│   ├── sensors/              # target-side statistical evidence
│   ├── source/               # source classifier/calibration/reference
│   └── tools/                # mature estimators, acquisition, OOD, registry
├── tests/                    # unit + smoke tests
└── pyproject.toml
```

## Quick start

Python 3.10+ is recommended.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
pip install -e .[dev]
```

Run the self-contained controlled demo:

```bash
statorch demo --out results/demo
```

Validate the repository and reported snapshots:

```bash
statorch validate
pytest -q
```

Regenerate frontend data from the structured result snapshot:

```bash
python scripts/export_frontend_data.py
```

Launch the frontend:

```bash
python scripts/serve_frontend.py --port 8000
```

Then open `http://127.0.0.1:8000`.

## Core runtime

The controller follows the invariant

```text
workspace
  -> statistical sensors
  -> typed state
  -> diagnosis scores
  -> contract-valid actions
  -> router / policy
  -> intervention
  -> recomputed state
  -> diagnostic check
  -> decision certificate
```

A certificate is an **audit record, not a correctness guarantee**. Online diagnostic improvement is kept separate from evaluator-only hidden task loss.

### Minimal API

```python
from statorch.agent.state import StatisticalState
from statorch.agent.contracts import ToolContract
from statorch.agent.certificate import DecisionCertificate
from statorch.tools.quantification import emq

beta = emq(target_proba, source_prior)
```

See `examples/minimal_api.py` and `examples/custom_tool.py`.

## Reported evidence snapshot

`results/reported/` mirrors the current manuscript's structured headline results, including:

- 1,232-unit controlled endpoint table;
- split-wise results;
- A0 → A1 → A2 measurement/stopping isolation;
- held-out adaptation / quantification / classification / open-world module routing;
- REALDISP and Gas Sensor Array Drift performance-cost summary;
- matched open-world directional response;
- saved fallback / HealthRule / Safe-threshold router artifacts.

These files are **reported-result snapshots**, not a substitute for unavailable raw experimental output. 

## External datasets

Raw REALDISP and Gas Sensor Array Drift data are not redistributed here. Protocol configs are included:

- REALDISP: train-subject ideal → train-subject self-placement calibration → held-out self-placement (moderate) / induced displacement (severe), budgets 1/3/5/9 sensors.
- Gas Drift: B1–B3 source → B4–B6 calibration → B7–B10 target, budgets 2/4/8/16 sensors.

The external adapters are intentionally dynamic in class/sensor count; they do not claim that a 5-class controlled-router checkpoint can be hard-transplanted to a 33-class sensor dataset.

## Claim discipline

Safe public wording is captured in `docs/claim_scope.md`. In particular, this project does **not** claim:

- universal learned-router superiority;
- oracle-optimal stopping;
- nominal sequential coverage from the bootstrap bands;
- calibrated unknown mass as a posterior probability;
- semantic novel-category discovery;
- unrestricted cross-domain generalization.

## Frontend

The dashboard is static HTML/CSS/JS and does not require npm. It exposes:

1. the evidence-grounded pipeline;
2. headline controlled metrics;
3. measurement/stopping mechanism isolation;
4. module oracle-headroom capture;
5. REALDISP / Gas Drift external boundaries;
6. an auditable example decision trace;
7. claim boundaries and reproducibility notes.


