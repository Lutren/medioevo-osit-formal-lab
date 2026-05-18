from __future__ import annotations

import math
from collections.abc import Sequence


def clamp01(x: float) -> float:
    """Clamp a numeric value to [0, 1]."""
    if math.isnan(x):
        raise ValueError("NaN is not a valid OSIT metric.")
    return max(0.0, min(1.0, float(x)))


def shannon_entropy(probabilities: Sequence[float], base: float = 2.0) -> float:
    """Compute Shannon entropy H(X) = -sum p log(p)."""
    if base <= 0 or base == 1:
        raise ValueError("Log base must be positive and not equal to 1.")

    total = sum(probabilities)
    if total <= 0:
        raise ValueError("Probability mass must be positive.")

    entropy = 0.0
    for p in probabilities:
        if p < 0:
            raise ValueError("Probabilities cannot be negative.")
        if p == 0:
            continue
        pn = p / total
        entropy -= pn * math.log(pn, base)

    return entropy


def normalized_entropy(probabilities: Sequence[float], base: float = 2.0) -> float:
    """Normalize Shannon entropy to [0, 1]."""
    n = len([p for p in probabilities if p > 0])
    if n <= 1:
        return 0.0

    h = shannon_entropy(probabilities, base=base)
    h_max = math.log(n, base)
    return clamp01(h / h_max)


def phi_eff_from_r(
    r: float,
    phi_0: float = 1.0,
    j_c: float = 1.0,
    exponent: float = 1.0,
) -> float:
    """Operational Phi_eff decay from residue R."""
    if j_c <= 0:
        raise ValueError("j_c must be positive.")
    if exponent <= 0:
        raise ValueError("exponent must be positive.")

    r = clamp01(r)
    if r >= j_c:
        return 0.0

    return clamp01(phi_0 * (1.0 - r / j_c) ** exponent)


def h_eff(h_x: float, phi_eff: float) -> float:
    """Usable information: H_eff(X|R) = H(X) * Phi_eff(R)."""
    if h_x < 0:
        raise ValueError("H(X) cannot be negative.")
    return h_x * clamp01(phi_eff)
