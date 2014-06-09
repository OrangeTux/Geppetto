from flask import Blueprint

router = Blueprint('gpio', __name__)


@router.route('/<int:gpio_nr>/setpoint', methods=['POST'])
def post_setpoint(gpio_id):
    """

    Enable or disable a GPIO pin.

    **Example Request**:

    .. sourcecode:: http

        POST /gpio/14/setpoint HTTP/1.1
        Accept: application/json
        Content-Type: application/json

        [
            {
                "value": 1
            }
        ]

    **Example Response**:

    .. sourcecode:: http

        HTTP/1.1 201 CREATED
        Content-Type: text/json

        [
            {
                "value": 1
            }
        ]

    :reqheader Accept: application/json
    :reqheader Content-Type: application/json
    :resheader Content-Type: application/json
    :statuscode 201: Setpoint created.
    :statuscode 400: Request body is invalid.
    :statuscode 404: GPIO pin doesn't exists.

    """
    pass
