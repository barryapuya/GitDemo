#any pytest file should start with test
#pytest method names should start with test
#Any code  should be wrapped  in method only
import pytest


@pytest.mark.smoke
def test_firstCreditCard():
    print("Hello")

@pytest.mark.xfail
def test_Greet():
    print("World")


def test_CrossBrowser(crossBrowser):
    print(crossBrowser[0])

