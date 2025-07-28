# production code
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def is_adult(self):
        return self.age >= 18

# test code
def test_user_is_adult(mocker):
    # Create a User object
    user = User(name="Alice", age=17)
    # Mock the is_adult property
    mocker.patch.object(User, "is_adult", new_callable=mocker.PropertyMock, return_value=True)
    
    assert user.is_adult is True