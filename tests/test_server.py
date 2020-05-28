import pytest
from src.artificial_intelligence import get_gayness_coefficient


@pytest.mark.parametrize(['name', 'result_min', 'result_max'],
                         [
                             pytest.param('Sanya', 0, 10),
                             pytest.param('Egor', 90, 100),
                             pytest.param('Enokenty', 0, 100)
                         ])
def test_ai(name, result_min, result_max):
    # Call SUT
    for i in range(100):
        val = get_gayness_coefficient(name)
        assert val >= result_min and val <= result_max
