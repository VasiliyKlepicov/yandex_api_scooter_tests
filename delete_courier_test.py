import sender_scooter_request


def test_delete_courier():
    courier_body = {
        "login": "ninja5",
        "password": "1234",
        "firstName": "saske"
     }
    sender_scooter_request.post_create_courier(courier_body)
    courier_login = {
        "login": "ninja5",
        "password": "1234"
    }
    post_courier_login_response = sender_scooter_request.post_courier_login(courier_login)
    courier_id = post_courier_login_response.json()['id']
    response = sender_scooter_request.delete_courier(courier_id)
    assert response.status_code == 200
    assert response


def test_delete_courier_no_courier_id():
    courier_id = ''
    response = sender_scooter_request.delete_courier(courier_id)
    assert response.status_code == 404
    assert response.json()['message'] == 'Not Found.'


def test_delete_courier_wrong_courier_id():
    courier_id = 123456
    response = sender_scooter_request.delete_courier(courier_id)
    assert response.status_code == 404
    assert response.json()['message'] == 'Курьера с таким id нет.'
