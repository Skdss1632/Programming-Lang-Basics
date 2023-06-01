import pytest
import sys


@pytest.mark.parametrize('username', 'password', [
    ('selenium', 'webdriver'),
    ('python', 'pytest'),
    ('mukesh', 'otwani')])
def test_login(username, password):
    print(username)
    print(password)