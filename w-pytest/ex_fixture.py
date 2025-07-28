import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


# Here’s roughly what’s happening if we were to do it by hand:    

# def fruit_bowl():
#     return [Fruit("apple"), Fruit("banana")]


# def test_fruit_salad(fruit_bowl):
#     # Act
#     fruit_salad = FruitSalad(*fruit_bowl)

#     # Assert
#     assert all(fruit.cubed for fruit in fruit_salad.fruit)


# # Arrange
# bowl = fruit_bowl()
# test_fruit_salad(fruit_bowl=bowl)


# Fixtures can request other fixtures

# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string_o(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]



# Fixtures are reusable

# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


def test_int(order):
    # Act
    order.append(2)

    # Assert
    assert order == ["a", 2]


# entry = first_entry()
# the_list = order(first_entry=entry)
# test_string(order=the_list)

# entry = first_entry()
# the_list = order(first_entry=entry)
# test_int(order=the_list)    

@pytest.fixture
def dynamic_fixture(request):
    param = request.param
    print(f"PAams =============== {param}")
    return param * 2

@pytest.mark.parametrize("dynamic_fixture", [2, 4, 6], indirect=True)
def test_with_dynamic_fixture(dynamic_fixture):
    assert dynamic_fixture in [4, 8, 12]


