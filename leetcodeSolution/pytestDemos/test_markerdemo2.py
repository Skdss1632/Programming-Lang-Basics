import pytest
import sys


@pytest.mark.skip
def test_login():
    print('login done')


@pytest.mark.skipif(sys.version_info < (3, 11), reason="requires python3.10 or higher")
def test_payment():
    print('add products')


@pytest.mark.xfail
def test_logout():
    assert False
    print('logout done')


def test_closeapplication():
    assert True
    print('close the application')


@pytest.mark.usefixtures
def test_usingfixtures():
    assert True
    print('close the application')