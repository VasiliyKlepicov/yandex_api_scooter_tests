import sender_scooter_request


def test_get_orders_no_courier_id():
    response = sender_scooter_request.get_orders_no_courier_id()
    assert response.status_code == 200


def test_get_orders():
    courier_body = {
       "login": "ninja1",
       "password": "1234",
       "firstName": "saske"
    }
    sender_scooter_request.post_create_courier(courier_body)
    courier_login = {
       "login": "ninja1",
       "password": "1234"
    }
    post_courier_login_response = sender_scooter_request.post_courier_login(courier_login)
    courier_id = post_courier_login_response.json()['id']
    response = sender_scooter_request.get_orders(courier_id)
    assert response.status_code == 200
