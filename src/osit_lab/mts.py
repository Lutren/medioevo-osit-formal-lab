from __future__ import annotations

import math
from dataclasses import dataclass

from osit_lab.measure_tools import clamp01


@dataclass(frozen=True)
class ResidueWeights:
    noise: float = 0.25
    latency: float = 0.15
    saturation: float = 0.20
    calibration: float = 0.15
    missing: float = 0.15
    contradiction: float = 0.10


@dataclass(frozen=True)
class ChannelResidue:
    noise: float = 0.0
    latency: float = 0.0
    saturation: float = 0.0
    calibration: float = 0.0
    missing: float = 0.0
    contradiction: float = 0.0


def channel_residue(
    residue: ChannelResidue,
    weights: ResidueWeights = ResidueWeights(),
) -> float:
    """Compute OSIT/MTS residue per channel."""
    return clamp01(
        weights.noise * clamp01(residue.noise)
        + weights.latency * clamp01(residue.latency)
        + weights.saturation * clamp01(residue.saturation)
        + weights.calibration * clamp01(residue.calibration)
        + weights.missing * clamp01(residue.missing)
        + weights.contradiction * clamp01(residue.contradiction)
    )


def channel_phi_eff(
    *,
    calibration_k: float,
    bandwidth_b: float,
    quality_q: float,
    r_i: float,
    tau_ms: float,
    tau_ref_ms: float,
    r_contradiction: float,
    alpha: float = 2.20,
    beta: float = 0.65,
    gamma: float = 0.70,
) -> float:
    """Compute Phi_eff_i for a calibrated channel."""
    if tau_ref_ms <= 0:
        raise ValueError("tau_ref_ms must be positive.")

    tau_norm = clamp01(tau_ms / tau_ref_ms)

    return clamp01(
        clamp01(calibration_k)
        * clamp01(bandwidth_b)
        * clamp01(quality_q)
        * math.exp(-alpha * clamp01(r_i))
        * math.exp(-beta * tau_norm)
        * (1.0 - gamma * clamp01(r_contradiction))
    )
