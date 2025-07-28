def person_details(person):
    name = person.name
    age = person.age

    return {"name": name, 'age': age}



def calculate_discount(price, discount_provider):
    discount = discount_provider.get_discount()
    return price - (price * discount / 100)


def test_calculate_discount(mocker):
    mock_discount_provider = mocker.Mock()

    mock_discount_provider.get_discount.return_value = 10

    result = calculate_discount(100, mock_discount_provider)

    assert result == 90

    mock_discount_provider.get_discount.assert_called_once()


def test_person_details(mocker):
    mock_person = mocker.Mock()

    mock_person.name = 'Mandeep'
    mock_person.age = 32

    result = person_details(mock_person)

    assert result['name'] == 'Mandeep' 


# nums = [1,2,3,4,5,6]

# for num in nums:
#     if num == 3:
#         break
# else: 
#     print("Done")