import pytest

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High priority
medium: Medium priority
low: Low priority
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line('markers',line)


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):  # injecao de dependencias - o pytest que injeta
    tmpdir = request.getfixturevalue("tmpdir")  # o pytest ja tem um diretorio temporario
    with tmpdir.as_cwd():  # changing working directory
        yield  # protocolo de generators
