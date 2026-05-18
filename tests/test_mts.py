import pytest

from osit_lab.mts import ChannelResidue, channel_phi_eff, channel_residue


def test_channel_residue_default_weights() -> None:
    r = channel_residue(ChannelResidue(noise=1.0))
    assert r == pytest.approx(0.25)


def test_channel_phi_eff_high_quality_low_residue() -> None:
    phi = channel_phi_eff(
        calibration_k=1.0,
        bandwidth_b=1.0,
        quality_q=1.0,
        r_i=0.0,
        tau_ms=0.0,
        tau_ref_ms=100.0,
        r_contradiction=0.0,
    )
    assert phi == pytest.approx(1.0)


def test_channel_phi_eff_degrades_with_residue() -> None:
    phi_low = channel_phi_eff(
        calibration_k=1.0,
        bandwidth_b=1.0,
        quality_q=1.0,
        r_i=0.8,
        tau_ms=0.0,
        tau_ref_ms=100.0,
        r_contradiction=0.0,
    )
    assert phi_low < 0.3
