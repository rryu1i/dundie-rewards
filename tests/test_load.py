import pytest
from dundie.core import load
from .constants import PEOPLE_FILE
import uuid
import os



@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people(request):
    """Test load function."""
    assert len(load(PEOPLE_FILE)) == 2



@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(request):
    """Test load function."""
    assert len(load(PEOPLE_FILE)) == 2



