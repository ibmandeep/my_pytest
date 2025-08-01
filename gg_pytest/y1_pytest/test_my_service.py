import pytest
from my_service import ApiClient, UserService


def get_api_client(mocker):
    mock_client = mocker.Mock(spec=ApiClient)

    mock_client.get_user_data.return_value = {"user_id": 1, "name": 'Singh'}

    service = UserService(mock_client)

    res = service.get_username(1)

    assert res == 'Singh'

    mock_client.get_user_data.assert_called_once_with(1)