# if we want to test only login func then we can use this flag:- pytest test_second.py -rA -k login
# if we want to summary of all the test case we can use this:-pytest -rA -v
def test_login():

    print('login to application')


def test_checkout():
    print('checkout')


def test_logout():
    print('logout from application')
