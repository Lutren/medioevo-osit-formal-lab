"""Synthetic MTS channel demo.

This file intentionally uses made-up channel inputs. It is a public-safe
demonstration of residue fusion, not a model of a real social, physical or
biological system.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from osit_lab.mts import ChannelResidue, channel_phi_eff, channel_residue  # noqa: E402


def main() -> None:
    synthetic_residue = ChannelResidue(
        noise=0.30,
        latency=0.20,
        saturation=0.10,
        calibration=0.15,
        missing=0.25,
        contradiction=0.05,
    )
    r_i = channel_residue(synthetic_residue)
    phi_eff_i = channel_phi_eff(
        calibration_k=0.90,
        bandwidth_b=0.80,
        quality_q=0.85,
        r_i=r_i,
        tau_ms=40.0,
        tau_ref_ms=120.0,
        r_contradiction=synthetic_residue.contradiction,
    )

    result = {
        "example": "mts_channel_demo",
        "input": {
            "channel": "synthetic-demo-channel",
            "R_noise": synthetic_residue.noise,
            "R_latency": synthetic_residue.latency,
            "R_missing": synthetic_residue.missing,
            "R_contradiction": synthetic_residue.contradiction,
        },
        "output": {
            "R_channel": r_i,
            "Phi_eff_channel": phi_eff_i,
        },
        "boundary": "synthetic channel only; no real telemetry; no deployment claim",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
