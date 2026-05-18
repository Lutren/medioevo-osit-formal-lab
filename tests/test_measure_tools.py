import math

import pytest

from osit_lab.measure_tools import (
    clamp01,
    h_eff,
    normalized_entropy,
    phi_eff_from_r,
    shannon_entropy,
)


def test_clamp01() -> None:
    assert clamp01(-1) == 0.0
    assert clamp01(0.5) == 0.5
    assert clamp01(2) == 1.0


def test_clamp01_rejects_nan() -> None:
    with pytest.raises(ValueError):
        clamp01(math.nan)


def test_shannon_entropy_fair_binary() -> None:
    assert shannon_entropy([0.5, 0.5]) == pytest.approx(1.0)


def test_normalized_entropy() -> None:
    assert normalized_entropy([1, 1, 1, 1]) == pytest.approx(1.0)
    assert normalized_entropy([1, 0, 0, 0]) == pytest.approx(0.0)


def test_phi_eff_decay() -> None:
    assert phi_eff_from_r(0.0) == pytest.approx(1.0)
    assert phi_eff_from_r(1.0) == pytest.approx(0.0)


def test_h_eff() -> None:
    assert h_eff(10.0, 0.5) == pytest.approx(5.0)
