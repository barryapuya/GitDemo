import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "barryapuya@gmail.com"]

@pytest.fixture(params=[("chrome", "Rahul", "Shetty"), ("Firexfox", "Shetty"), ("IE", "SS")])
def crossBrowser(request):
    return request.param


