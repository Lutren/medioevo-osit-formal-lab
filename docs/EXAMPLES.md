# Minimal Examples

These examples are intentionally small and synthetic. They demonstrate how to
call the public-safe OSIT Formal Lab APIs without using private MEDIOEVO
material, real datasets, internal prompts or deployment runtime.

Run from the repository root:

```bash
python examples/basic_measure_tools.py
python examples/mts_channel_demo.py
python examples/gates_demo.py
```

## `basic_measure_tools.py`

Shows:

- `clamp01`;
- a simple normalized residue value;
- `Phi_eff` decay from residue;
- normalized entropy and `H_eff`.

The input distribution is synthetic. It is not a measurement of a real system.

## `mts_channel_demo.py`

Shows:

- a synthetic MTS channel;
- `R_noise`, `R_latency`, `R_missing` and contradiction residue;
- a fused channel residue;
- a channel `Phi_eff` value.

The channel is a toy example only.

## `gates_demo.py`

Shows:

- channel gate output: `APPROVE`, `REVIEW` or `BLOCK`;
- a conservative ScienceClaimGate-style boundary example;
- a blocked example for overclaiming.

The gate examples are release discipline tools. They are not proof of a
scientific theory.
