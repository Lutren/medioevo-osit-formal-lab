from __future__ import annotations

from enum import StrEnum

from osit_lab.measure_tools import clamp01


class GateStatus(StrEnum):
    APPROVE = "APPROVE"
    REVIEW = "REVIEW"
    BLOCK = "BLOCK"


def channel_gate(
    *,
    r_sens: float,
    phi_eff_i: float,
    r_i: float,
    r_contradiction_i: float,
) -> GateStatus:
    """Apply OSIT channel gate logic."""
    r_sens = clamp01(r_sens)
    phi_eff_i = clamp01(phi_eff_i)
    r_i = clamp01(r_i)
    r_contradiction_i = clamp01(r_contradiction_i)

    if r_sens >= 0.80:
        return GateStatus.BLOCK
    if phi_eff_i < 0.60:
        return GateStatus.BLOCK
    if r_i >= 0.60:
        return GateStatus.REVIEW
    if r_contradiction_i >= 0.50:
        return GateStatus.REVIEW
    if r_sens >= 0.50:
        return GateStatus.REVIEW

    return GateStatus.APPROVE
