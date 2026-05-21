import os

import pytest


@pytest.mark.integration
def test_integration_requires_running_server():
    if not os.environ.get("KAVE_INTEGRATION"):
        pytest.skip("set KAVE_INTEGRATION=1 with kave-server:dev running")
