import sender_scooter_request
import data


def test_get_all_orders():
    response = sender_scooter_request.get_all_orders()
    assert response.status_code == 200


def test_get_orders_courier_id():
    courier_body = data.courier_body
    sender_scooter_request.create_courier(courier_body)
    courier_login = data.courier_login
    post_courier_login_response = sender_scooter_request.post_courier_login(courier_login)
    courier_id = post_courier_login_response.json()['id']
    response = sender_scooter_request.get_orders_courier_id(courier_id)
    assert response.status_code == 200
    assert response.json()
    delete_courier_response = sender_scooter_request.delete_courier(courier_id)
    assert delete_courier_response.status_code == 200
    assert delete_courier_response


def test_get_orders_wrong_courier_id():
    courier_id = 123456
    response = sender_scooter_request.get_orders_courier_id(courier_id)
    assert response.status_code == 404
    assert response.json()['message'] == 'Курьер с идентификатором 123456 не найден'
