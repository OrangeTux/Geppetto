from quick2wire.gpio import pins, Out
from logbook import Logger

log = Logger(__name__)


def set_pin(pin_nr, value):
    """ Write HIGH or LOW to GPIO pin.

    :param pin_nr: BOARD pin number.
    :param vaue: Value.

    """
    pin = pins.pin(pin_nr, direction=Out)

    with pin:
        pin.value = int(value)
        log.debug('Wrote %d to pin %d.' % (value, pin_nr))

        return pin.value
