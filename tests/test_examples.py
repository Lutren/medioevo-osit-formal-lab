from __future__ import annotations

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_basic_measure_tools_example_runs() -> None:
    runpy.run_path(str(ROOT / "examples" / "basic_measure_tools.py"), run_name="__main__")


def test_mts_channel_demo_runs() -> None:
    runpy.run_path(str(ROOT / "examples" / "mts_channel_demo.py"), run_name="__main__")


def test_gates_demo_runs() -> None:
    runpy.run_path(str(ROOT / "examples" / "gates_demo.py"), run_name="__main__")
