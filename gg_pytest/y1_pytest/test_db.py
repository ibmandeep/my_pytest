import pytest
from db import DataBase


@pytest.fixture
def db():
    database = DataBase()
    yield database
    database.users.clear() #this will always run after each test

def test_add_user(db):
    db.add_user(1, "Mandeep")

    assert db.get_user(1) == "Mandeep"

def test_add_dublicate_user(db):
    db.add_user(1,"Mandeep")
    
    with pytest.raises(ValueError):
        db.add_user(1,"Singh")


def test_delete_user(db):
    db.add_user(1,"Mandeep")
    db.delete_user(1)

    assert db.get_user(1) is None