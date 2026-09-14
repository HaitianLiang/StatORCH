# Architecture

StatOrch separates **evidence generation** from **orchestration**.

```text
Data / source knowledge
        ↓
Statistical sensors
        ↓
Typed StatisticalState
        ↓
Diagnosis scores + contracts
        ↓
Valid action set
        ↓
Router / acquisition policy
        ↓
Tool execution
        ↓
State refresh + predeclared diagnostic check
        ↓
DecisionCertificate
        ↺
```

The core state is partitioned into:

- `B`: population estimates (`beta`, optional open-mass proxy);
- `U`: bootstrap uncertainty summaries;
- `D`: source–target discrepancy;
- `F`: fit and residual diagnostics;
- `R`: representation health;
- `O`: out-of-reference evidence;
- `I`: value-of-information / acquisition evidence;
- `C`: remaining measurement/compute budget;
- `H`: tool health and history.

## Contracts

A tool contract records:

```text
requirements
preconditions
outputs
target diagnostics
cost
failure modes
```

Validity is checked before utility. A router cannot select a tool whose contract is not satisfied.

## Verification

A nonterminal action declares oriented target diagnostics and guard diagnostics. The verifier compares pre/post values and returns one of:

- `diagnostic-supported`
- `diagnostic-unsupported`
- `inconclusive`

This is an online observable check, not a guarantee of hidden task-loss improvement.
