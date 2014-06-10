from app.tasks import set_pin


def test_set_pin():
    """ Test set_pin. """
    assert set_pin(3, 0) is False
    assert set_pin(3, 1) is True
