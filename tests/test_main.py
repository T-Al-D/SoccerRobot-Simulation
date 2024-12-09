"""!
@file 
@brief some basic testing for the python code
"""

import pytest
from main import runSimulation


# Run this test for a certain amount of ms
@pytest.mark.parametrize("durationInMs", [2500])
def test_runSimulationForDuration(durationInMs):
    try:
        runSimulation(True, durationInMs)
        # If the function completes successfully, the game loop ran for the specified time
        assert True  # Just check that the function runs without crashing
    except Exception as e:
        pytest.fail(f"Main loop failed to run for {durationInMs}ms: {e}")
