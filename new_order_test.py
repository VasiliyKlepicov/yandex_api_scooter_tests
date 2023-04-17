import sender_scooter_request
import data


def test_new_order():
    order_body = data.order_body
    response = sender_scooter_request.new_order(order_body)
    assert response.status_code == 201
    assert response.json()['track'] != 0
