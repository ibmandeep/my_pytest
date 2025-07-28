# content of conftest.py
import smtplib

import pytest

# Scope: sharing fixtures across classes, modules, packages or session
# Possible values for scope are: function, class, module, package or session.

@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


# def pytest_addoption(parser):
#     parser.addoption(
#         "--stringinput",
#         action="append",
#         default=[],
#         help="list of stringinputs to pass to test functions",
#     )

# def pytest_generate_tests(metafunc):
#     if "stringinput" in metafunc.fixturenames:
#         metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))


def pytest_addoption(parser):
    parser.addoption(
        "--env",  # custom option
        action="store",  # take value like --env=staging
        default="dev",  # default value if not passed
        help="Environment to run tests against: dev, staging, prod"
    )

@pytest.fixture
def env(request):
    return request.config.getoption("--env")    
    