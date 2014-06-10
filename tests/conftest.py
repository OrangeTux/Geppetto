import pytest

from app import app as application


@pytest.fixture
def client():
    """ Return test instance of app. """
    return application.test_client()
