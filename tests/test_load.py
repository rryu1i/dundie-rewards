import pytest
from dundie.core import load
from .constants import PEOPLE_FILE
import uuid
import os


@pytest.fixture(scope="function", autouse=True)  # se tiver autouse = True,
#todos os testes dentro desse arquivo irao usar essa fixture,
# caso queira aplicar apenas em determinada function, tirar o autouse e
# fazer o test_load receber create_new_file
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("isso 'e sujeira...")
    yield
    file_.remove()


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function."""

    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))  # apos finalizar o test
    # o os.unlink apaga o arquivo, mesma coisa que utilizar a fixture acima.

    with open(filepath, "w") as f:
        f.write("Dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'


@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test load function."""

    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as f:
        f.write("Dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'

