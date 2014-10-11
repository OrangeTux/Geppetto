import os
import mock
from quick2wire.gpio import pins, Out
from logbook import Logger

from . import app

log = Logger(__name__)


def get_pin(pin_nr, direction):
    """ Return Mock of pin when file descriptor of pin doesn't exists and
    MOCK_PINS settings has been enabled.

    :param pin_nr: Number of pin.
    :param direction: The direction, quick2wire.gpio.In or quick2wire.gpio.Out.
    :return: Pin or Mock instance.

    """
    pin = pins.pin(pin_nr, direction=direction)
    if not os.path.exists(pin._pin_path()) and\
            app.config.get('MOCK_PINS', False):

        return mock.MagicMock()

    return pin


def set_pin_value(pin_nr, value):
    """ Write HIGH or LOW to GPIO pin.

    :param pin_nr: BOARD pin number.
    :param vaue: Value.

    """
    pin = get_pin(pin_nr, direction=Out)

    with pin:
        pin.value = int(value)
        log.debug('Wrote %d to pin %d.' % (value, pin_nr))

        return pin.value
