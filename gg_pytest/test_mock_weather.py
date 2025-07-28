def fetch_weather_data(api_client):
    response = api_client.get("https://api.weather.com/data")
    if response.status_code == 200:
        return response.json()
    else:
        return None



def test_fetch_weather_data(mocker):
    # Create a mock API client
    mock_api_client = mocker.Mock()

    # Mock the response of the API client
    mock_responce = mocker.Mock()
    mock_responce.status_code = 200
    mock_responce.json.return_value = {"temperature": "20C", "condition": "Sunny"}

    # Set the mock API client to return the mocked response
    mock_api_client.get.return_value = mock_responce

    result = fetch_weather_data(mock_api_client)

    assert result == {"temperature": "20C", "condition": "Sunny"}

    #checks that the get method of the mock API client was called exactly once and with the correct argument.
    mock_api_client.get.assert_called_once_with("https://api.weather.com/data")