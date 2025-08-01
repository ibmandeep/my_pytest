import pytest
from user_manager import UserManager


# def test_add_user():
#     user_manager = UserManager()
#     assert user_manager.add_user('Mandeep', "mandeep@mail.com") == True
#     assert user_manager.get_user('Mandeep') == "mandeep@mail.com"

@pytest.fixture
def user_manager():
    """Create a fresh instance of UserManager before each test"""
    return UserManager()


def test_get_user(user_manager):
    assert user_manager.add_user('Mandeep', "mandeep@mail.com") == True
    assert user_manager.get_user('Mandeep') == "mandeep@mail.com"

def test_add_user_n(user_manager):
    user_manager.add_user('Mandeep', "mandeep@mail.com")

    with pytest.raises(ValueError):
        user_manager.add_user('Mandeep', "singh@mail.com")
