import json
from flask import Blueprint, abort, request, jsonify
from flask.ext.login import login_required

from app.tasks import set_pin_value

router = Blueprint('gpio', __name__)


@router.route('/<int:pin_nr>/setpoint', methods=['POST'])
@login_required
def post_setpoint(pin_nr):
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

        HTTP/1.1 200 SUCCESS
        Content-Type: text/json

        {
            "value": 1
        }

    :reqheader Accept: application/json
    :reqheader Content-Type: application/json
    :resheader Content-Type: application/json
    :statuscode 200: Success
    :statuscode 400: Request body is invalid.
    :statuscode 403: Unauthorized.
    :statuscode 404: GPIO pin doesn't exists.
    :statuscode 422: Request body is not valid JSON.

    """
    try:
        data = json.loads(request.data.decode('utf8'))
    except:
        abort(422)

    if 'value' not in data or data['value'] not in [0, 1]:
        abort(400)

    try:
        set_pin_value(pin_nr, data['value'])
    except IndexError:
        abort(404)

    return jsonify(data)
