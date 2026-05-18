"""Gate examples for public-safe OSIT usage.

The ScienceClaimGate in this example is deliberately conservative. It shows
how public writing can be downgraded to REVIEW or BLOCK before publication.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from osit_lab.gates import GateStatus, channel_gate  # noqa: E402


def science_claim_gate(claim: str) -> GateStatus:
    lowered = claim.lower()
    blocked_terms = (
        "resolved physics",
        "prediction guarantee",
        "agi completion",
        "fairness guarantee",
    )
    if any(term in lowered for term in blocked_terms):
        return GateStatus.BLOCK
    if "evidence" not in lowered and "synthetic" not in lowered:
        return GateStatus.REVIEW
    return GateStatus.APPROVE


def main() -> None:
    channel_decision = channel_gate(
        r_sens=0.20,
        phi_eff_i=0.72,
        r_i=0.25,
        r_contradiction_i=0.10,
    )
    public_claim = "This synthetic example shows an operational gate with evidence."

    result = {
        "example": "gates_demo",
        "channel_gate": channel_decision.value,
        "science_claim_gate": science_claim_gate(public_claim).value,
        "blocked_claim_gate": science_claim_gate("prediction guarantee").value,
        "boundary": "examples can be APPROVE/REVIEW/BLOCK, but publication claims stay gated",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
