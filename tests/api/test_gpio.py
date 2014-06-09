import json


def test_post_setpoint_422(client):
    """ Test for 422 response code.  """
    with client as cl:
        res = cl.post('/gpio/3/setpoint')

        assert res.status_code == 422


def test_post_setpoint_400(client):
    """ Test for 400 response code. """
    with client as cl:
        res = cl.post('/gpio/3/setpoint',
                      data=json.dumps({'invalid_key': 3}))

        assert res.status_code == 400

        res = cl.post('/gpio/3/setpoint',
                      data=json.dumps({'id': 3}))

        assert res.status_code == 400
