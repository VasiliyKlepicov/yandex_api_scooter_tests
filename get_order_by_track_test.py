import sender_scooter_request
import data


def test_get_order_by_track():
    order_body = data.order_body
    post_new_order_response = sender_scooter_request.post_new_order(order_body)
    track = post_new_order_response.json()['track']
    response = sender_scooter_request.get_order_by_track(track)
    assert response.status_code == 200


def test_get_order_by_wrong_track():
    track = 123456
    response = sender_scooter_request.get_order_by_track(track)
    assert response.status_code == 404
    assert response.json()['message'] == 'Заказ не найден'


def test_get_order_by_empty_track():
    track = ''
    response = sender_scooter_request.get_order_by_track(track)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для поиска'
