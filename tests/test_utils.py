import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["roger.issonaga@gmail.com", "kekimus@gmail.com", "kek@kek.kek"]
)
def test_positive_check_valid_email(address):
    """Ensure email is valid."""
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["roger.issonaga@.com", "@gmail.com", "kek@kek"]
)
def test_negative_check_valid_email(address):
    """Ensure email is invalid."""
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    """Test generation of random simple passwords"""
    passwords = []
    for i in range(100):
        passwords.append(generate_simple_password(8))
    assert len(set(passwords)) == 100  # set tira duplicados
