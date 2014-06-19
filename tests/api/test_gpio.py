import json


def test_post_setpoint_422(client, auth_header):
    """ Test for 422 response code.  """
    with client as cl:
        res = cl.post('/gpio/3/setpoint', headers=auth_header)

        assert res.status_code == 422


def test_post_setpoint_400(client, auth_header):
    """ Test for 400 response code. """
    with client as cl:
        res = cl.post('/gpio/3/setpoint',
                      headers=auth_header,
                      data=json.dumps({'invalid_key': 3}))

        assert res.status_code == 400

        res = cl.post('/gpio/3/setpoint',
                      headers=auth_header,
                      data=json.dumps({'id': 3}))

        assert res.status_code == 400


def test_post_setpoint_404(client, auth_header):
    """ Test for 404 response code. """
    with client as cl:
        res = cl.post('/gpio/29/setpoint',
                      headers=auth_header,
                      data=json.dumps({'value': 1}))

        assert res.status_code == 404


def test_post_setpoint_200(client, auth_header):
    """ Test for 200 response code. """
    data = json.dumps({'value': 1})
    with client as cl:
        res = cl.post('/gpio/3/setpoint',
                      headers=auth_header,
                      data=data)

        assert res.status_code == 200
        assert res.data.decode('utf8') == data
