# MEDIOEVO / OSIT Formal Lab

Formal lab for operational information metrics used in the public-safe MEDIOEVO / OSIT layer.

This repository is not a claim that OSIT proves universal physics, consciousness, AGI, or a replacement for Shannon information theory. It is a reproducible lab for testing operational metrics:

- Shannon entropy
- normalized residue `R`
- effective update/integration `Phi_eff`
- usable information `H_eff`
- MTS channel residue
- MTS channel `Phi_eff`
- channel gates: `APPROVE`, `REVIEW`, `BLOCK`

## Core Equation

```text
H_eff(X | R) = H(X) * Phi_eff(R)
```

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

## Test

```bash
make ci
```

or:

```bash
python -m pytest -q
python -m ruff check src tests
python -m mypy src
```

## Minimal Examples

The `examples/` folder contains small synthetic demos:

- `basic_measure_tools.py`: `clamp01`, normalized residue, `Phi_eff` and `H_eff`.
- `mts_channel_demo.py`: synthetic MTS channel residue and channel `Phi_eff`.
- `gates_demo.py`: `APPROVE` / `REVIEW` / `BLOCK` examples with a conservative claim boundary.

Run them from the repository root:

```bash
python examples/basic_measure_tools.py
python examples/mts_channel_demo.py
python examples/gates_demo.py
```

See `docs/EXAMPLES.md` and `docs/USAGE_BOUNDARY.md` for the public-safe usage boundary.

## Boundary

Public-safe language:

```text
OSIT is an operational method for state-aware agents with residue, evidence, gates and continuity.
```

Blocked language:

```text
Any wording that asserts resolved physics, consciousness, AGI or prediction guarantees.
```

## Repository Role

This lab is the reproducible measurement lane. It does not include private MEDIOEVO books, RPG/TCG assets, Claudio/Wabi/DUAT private runtime, raw prompts, real datasets, secrets, credentials or proprietary calibration material.
