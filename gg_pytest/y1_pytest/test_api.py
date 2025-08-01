import pytest
from api import app


@pytest.fixture
def client():
    app.config['TESTING']= True

    with app.test_client() as client:
        yield client


def test_add_user(client):
    res = client.post('/users', json={"id": 1, "name": "Mandeep"})

    assert res.status_code == 201
    assert res.json == {"id": 1, "name": "Mandeep"}

def test_add_user_invaild_data(client):
    res = client.post('/users', json={"id": 4})

    assert res.status_code == 400
    assert res.json.get('error') == "Invaild data"

def test_add_user_alredy_exist(client):
    client.post('/users', json={"id": 5, "name": "Singh"})

    res = client.post('/users', json={"id": 5, "name": "Singh"})
    assert res.status_code == 400
    assert res.json.get('error') == "User alredy exists"

def test_get_user(client):
    """Test retrieving a user""" 
    #first add the user
    client.post('/users', json={"id": 2, "name": "Singh"})

    res = client.get('/users/2')

    assert res.status_code == 200
    assert res.json == {"id": 2, "name": "Singh"}


def test_get_user_not_found(client):
    res = client.get('/users/3')

    assert res.status_code == 404
    assert res.json.get('error') == 'User not found.'
