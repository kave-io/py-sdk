from pathlib import Path

import pytest


@pytest.mark.contract
def test_contract_scenarios_are_present():
    scenarios = Path(__file__).resolve().parents[2] / "contract-tests" / "scenarios"
    assert scenarios.exists()
    assert any(scenarios.glob("*.yaml"))
