from osit_lab.gates import GateStatus, channel_gate


def test_channel_gate_approve() -> None:
    assert (
        channel_gate(
            r_sens=0.0,
            phi_eff_i=0.9,
            r_i=0.1,
            r_contradiction_i=0.0,
        )
        == GateStatus.APPROVE
    )


def test_channel_gate_review_on_contradiction() -> None:
    assert (
        channel_gate(
            r_sens=0.0,
            phi_eff_i=0.9,
            r_i=0.1,
            r_contradiction_i=0.6,
        )
        == GateStatus.REVIEW
    )


def test_channel_gate_block_on_low_phi() -> None:
    assert (
        channel_gate(
            r_sens=0.0,
            phi_eff_i=0.5,
            r_i=0.1,
            r_contradiction_i=0.0,
        )
        == GateStatus.BLOCK
    )
