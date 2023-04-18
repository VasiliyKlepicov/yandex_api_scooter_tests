import sender_scooter_request
import data


def test_create_courier():
    courier_body = data.courier_body
    response = sender_scooter_request.create_courier(courier_body)
    assert response.status_code == 201
    assert response


def test_create_courier_no_login():
    courier_body = {
        "login": "",
        "password": "1234",
        "firstName": "saske"
    }
    response = sender_scooter_request.create_courier(courier_body)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'


def test_create_courier_no_password():
    courier_body = {
        "login": "ninja",
        "password": "",
        "firstName": "saske"
    }
    response = sender_scooter_request.create_courier(courier_body)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'


def test_create_courier_duplicate_login():
    courier_body = data.courier_body
    response = sender_scooter_request.create_courier(courier_body)
    assert response.status_code == 409
    assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
    courier_login = data.courier_login
    post_courier_login_response = sender_scooter_request.post_courier_login(courier_login)
    courier_id = post_courier_login_response.json()['id']
    delete_courier_response = sender_scooter_request.delete_courier(courier_id)
    assert delete_courier_response.status_code == 200
    assert delete_courier_response
