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

## Boundary

Public-safe language:

```text
OSIT is an operational method for state-aware agents with residue, evidence, gates and continuity.
```

Blocked language:

```text
OSIT proves physics, consciousness, AGI or guaranteed prediction.
```

## Repository Role

This lab is the reproducible measurement lane. It does not include private MEDIOEVO books, RPG/TCG assets, Claudio/Wabi/DUAT private runtime, raw prompts, real datasets, secrets, credentials or proprietary calibration material.

