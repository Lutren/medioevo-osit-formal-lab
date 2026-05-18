"""Minimal public-safe examples for OSIT measure tools.

The values are synthetic and only demonstrate the API surface. They are not
real-world measurements and do not make predictive claims.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from osit_lab.measure_tools import clamp01, h_eff, normalized_entropy, phi_eff_from_r  # noqa: E402


def main() -> None:
    raw_residue = 0.32
    r = clamp01(raw_residue)
    phi_eff = phi_eff_from_r(r, phi_0=1.0, j_c=1.0, exponent=1.0)
    h_x = normalized_entropy([3.0, 1.0, 0.5, 0.5])

    result = {
        "example": "basic_measure_tools",
        "input": {
            "raw_residue": raw_residue,
            "synthetic_distribution": [3.0, 1.0, 0.5, 0.5],
        },
        "output": {
            "R": r,
            "Phi_eff": phi_eff,
            "H_normalized": h_x,
            "H_eff": h_eff(h_x, phi_eff),
        },
        "boundary": "synthetic example; no real dataset; no prediction claim",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
