import time
def long_running_task():
    time.sleep(5)  # Simulate a long delay
    return "Task Complete"

# test code
def test_long_running_task(mocker):
    # Mock the sleep function in the time module
    mocker.patch("time.sleep", return_value=None)
    # Call the function
    result = long_running_task()
    # Assert the result is correct
    assert result == "Task Complete"