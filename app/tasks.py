from gpiocrust import Header, OutputPin
from logbook import Logger

log = Logger(__name__)


def set_pin(pin_nr, value):
    """ Write HIGH or LOW to GPIO pin.

    :param pin_nr: BOARD pin number.
    :param vaue: Value.

    """
    with Header():
        p = OutputPin(pin_nr, value=bool(value))
        log.debug('Wrote %d to pin %d.' % (value, pin_nr))

        return p.value
