import json
from flask import Blueprint, abort, request

#from tasks import set_pin
#from utils import get_pin

router = Blueprint('gpio', __name__)


@router.route('/<int:gpio_nr>/setpoint', methods=['POST'])
def post_setpoint(gpio_nr):
    """

    Enable or disable a GPIO pin.

    **Example Request**:

    .. sourcecode:: http

        POST /gpio/14/setpoint HTTP/1.1
        Accept: application/json
        Content-Type: application/json

        {
            "value": 1
        }

    **Example Response**:

    .. sourcecode:: http

        HTTP/1.1 200 SUCCES
        Content-Type: text/json

        {
            "value": 1
        }

    :reqheader Accept: application/json
    :reqheader Content-Type: application/json
    :resheader Content-Type: application/json
    :statuscode 200: Succes
    :statuscode 400: Request body is invalid.
    :statuscode 404: GPIO pin doesn't exists.
    :statuscode 422: Request body is not valid JSON.

    """
    try:
        data = json.loads(request.data)
    except:
        abort(422)

    if 'value' not in data or data['value'] not in [0, 1]:
        abort(400)

    try:
        #pin = get_pin(gpio_nr)
        pass
    except KeyError:
        abort(404)

    #set_pin(pin, data['value'])

    return request.data
