import sender_scooter_request


def test_create_courier():
    courier_body = {
        "login": "ninja2",
        "password": "1234",
        "firstName": "saske"
     }
    response = sender_scooter_request.post_create_courier(courier_body)
    assert response.status_code == 201
    assert response


def test_create_courier_no_login_no_password():
    courier_body = {
        "login": "",
        "password": "",
        "firstName": "saske"
    }
    response = sender_scooter_request.post_create_courier(courier_body)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'


def test_create_courier_duplicate_login():
    courier_body = {
        "login": "ninja2",
        "password": "1234",
        "firstName": "saske"
     }
    response = sender_scooter_request.post_create_courier(courier_body)
    assert response.status_code == 409
    assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
