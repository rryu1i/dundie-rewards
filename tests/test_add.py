import pytest

from dundie.core import add
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_add_movement():
    db = connect()

    pk = "joe@doe.com"
    data = {"name": "Joe Doe", "role": "Salesman", "dept": "Sales"}
    _, created = add_person(db, pk, data)  # o _ era person, mas nao sera usado
    assert created is True

    pk = "jim@doe.com"
    data = {"name": "Jim Doe", "role": "Manager", "dept": "Management"}
    _, created = add_person(db, pk, data)  # o _ era person, mas nao sera usado
    assert created is True

    commit(db)

    add(-30, email="joe@doe.com")
    add(90, dept="Management")

    db = connect()
    assert db["balance"]["joe@doe.com"] == 470
    assert db["balance"]["jim@doe.com"] == 190
