import mock
from quick2wire.gpio import Pin, Out
from app.tasks import set_pin_value, get_pin
from app import app


def test_get_pin_without_mocking_pins(monkeypatch):
    """ Test `app.tasks.get_pin` with MOCK_PINS set to False. """
    monkeypatch.setattr('os.path.exists', lambda x: True)

    app.config['MOCK_PINS'] = False
    assert type(get_pin(1, Out)) == Pin
    app.config['MOCK_PINS'] = True

    monkeypatch.undo()


def test_get_pin_with_mocking_pins():
    """ Test `app.tasks.get_pin` with MOCK_PINS set to True. """
    assert isinstance(get_pin(1, Out), mock.MagicMock)


def test_set_pin_value():
    assert set_pin_value(3, 0) is 0
    assert set_pin_value(3, 1) is 1
