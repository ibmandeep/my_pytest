# def test_valid_string(stringinput):
#     assert stringinput.isalpha()



def test_environment(env):
    assert env in ["dev", "staging", "prod"]    