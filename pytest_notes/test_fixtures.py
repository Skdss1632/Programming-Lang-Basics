import pytest


# @pytest.fixture()
# def setup():
#     print('start browser')
#
#
# def test_1(setup):
#     print('start browser')
#     print('test 1 executed')
#     print('close browser')
#
#
# def test_2(setup):
#     print('start browser')
#     print('test 2 executed')
#     print('close browser')
#
#
# def test_3(setup):
#     print('start browser')
#     print('test 3 executed')
#     print('close browser')

# ..........................................................................................................................

@pytest.fixture()
def setup():
    print('start browser')
    yield
    print('close browser')


def test_1(setup):

    print('test 1 executed')


def test_2(setup):

    print('test 2 executed')


def test_3(setup):

    print('test 3 executed')


