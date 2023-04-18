import sender_scooter_request
import data


def test_cancel_order():
    order_body = data.order_body
    post_new_order_response = sender_scooter_request.new_order(order_body)
    track = post_new_order_response.json()['track']
    response = sender_scooter_request.cancel_order(track)
    assert response.status_code == 200
    assert response


def test_cancel_order_by_empty_track():
    track = ''
    response = sender_scooter_request.cancel_order(track)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для поиска'


def test_cancel_order_by_wrong_track():
    track = 123456
    response = sender_scooter_request.get_order_by_track(track)
    assert response.status_code == 404
    assert response.json()['message'] == 'Заказ не найден'


def test_cancel_order_in_progress():
    courier_body = data.courier_body
    sender_scooter_request.create_courier(courier_body)
    courier_login = data.courier_login
    post_courier_login_response = sender_scooter_request.post_courier_login(courier_login)
    courier_id = post_courier_login_response.json()['id']
    order_body = data.order_body
    post_new_order_response = sender_scooter_request.new_order(order_body)
    track = post_new_order_response.json()['track']
    get_order_by_track_response = sender_scooter_request.get_order_by_track(track)
    order_id = get_order_by_track_response.json()['order']['id']
    response = sender_scooter_request.accept_order(order_id, courier_id)
    assert response.status_code == 200
    assert response
    response = sender_scooter_request.cancel_order(track)
    assert response.status_code == 409
    assert response.json()['message'] == 'Заказ нельзя завершить'
    delete_courier_response = sender_scooter_request.delete_courier(courier_id)
    assert delete_courier_response.status_code == 200
    assert delete_courier_response
