import sender_scooter_request
import data


def test_courier_login():
    courier_body = data.courier_body
    sender_scooter_request.create_courier(courier_body)
    courier_login = data.courier_login
    response = sender_scooter_request.post_courier_login(courier_login)
    assert response.status_code == 200
    assert response.json()['id'] != 0
    courier_id = response.json()['id']
    delete_courier_response = sender_scooter_request.delete_courier(courier_id)
    assert delete_courier_response.status_code == 200
    assert delete_courier_response


def test_courier_login_no_login_no_password():
    courier_login = {
        "login": "",
        "password": ""
    }
    response = sender_scooter_request.post_courier_login(courier_login)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для входа'


def test_courier_login_wrong_login_wrong_password():
    courier_login = {
        "login": "abcdef",
        "password": "abcdef"
    }
    response = sender_scooter_request.post_courier_login(courier_login)
    assert response.status_code == 404
    assert response.json()['message'] == 'Учетная запись не найдена'
