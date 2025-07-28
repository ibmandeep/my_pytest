# content of test_module.py

# Here, the test_ehlo needs the smtp_connection fixture value. pytest will discover and 
# call the @pytest.fixture marked smtp_connection fixture function.
# You see the two assert 0 failing and more importantly you can also see that the exactly 
# same smtp_connection object was passed into the two test functions because 
# pytest shows the incoming argument values in the traceback.


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes