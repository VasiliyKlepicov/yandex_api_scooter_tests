import sender_scooter_request
import data


def test_finish_order():
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