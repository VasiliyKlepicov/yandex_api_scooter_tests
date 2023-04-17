import sender_scooter_request


def test_post_courier_login():
    courier_body = {
        "login": "ninja3",
        "password": "1234",
        "firstName": "saske"
     }
    sender_scooter_request.post_create_courier(courier_body)
    courier_login = {
        "login": "ninja3",
        "password": "1234"
    }
    response = sender_scooter_request.post_courier_login(courier_login)
    assert response.status_code == 200
    assert response.json()['id'] != 0


def test_post_courier_login_no_login_no_password():
    courier_login = {
        "login": "",
        "password": ""
    }
    response = sender_scooter_request.post_courier_login(courier_login)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для входа'


def test_post_courier_login_wrong_login_wrong_password():
    courier_login = {
        "login": "abcdef",
        "password": "abcdef"
    }
    response = sender_scooter_request.post_courier_login(courier_login)
    assert response.status_code == 404
    assert response.json()['message'] == 'Учетная запись не найдена'
