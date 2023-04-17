import sender_scooter_request
import data


def test_accept_order():
    courier_body = {
       "login": "ninja4",
       "password": "1234",
       "firstName": "saske"
    }
    sender_scooter_request.post_create_courier(courier_body)
    courier_login = {
       "login": "ninja4",
       "password": "1234"
    }
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


def test_accept_no_order_id():
    courier_body = {
       "login": "ninja4",
       "password": "1234",
       "firstName": "saske"
    }
    sender_scooter_request.post_create_courier(courier_body)
    courier_login = {
       "login": "ninja4",
       "password": "1234"
    }
    post_courier_login_response = sender_scooter_request.post_courier_login(courier_login)
    courier_id = post_courier_login_response.json()['id']
    order_body = data.order_body
    post_new_order_response = sender_scooter_request.new_order(order_body)
    track = post_new_order_response.json()['track']
    sender_scooter_request.get_order_by_track(track)
    order_id = ''
    response = sender_scooter_request.accept_order(order_id, courier_id)
    assert response.status_code == 404
    assert response.json()['message'] == 'Not Found.'


def test_accept_wrong_order_id():
    courier_body = {
       "login": "ninja4",
       "password": "1234",
       "firstName": "saske"
    }
    sender_scooter_request.post_create_courier(courier_body)
    courier_login = {
       "login": "ninja4",
       "password": "1234"
    }
    post_courier_login_response = sender_scooter_request.post_courier_login(courier_login)
    courier_id = post_courier_login_response.json()['id']
    order_body = data.order_body
    post_new_order_response = sender_scooter_request.new_order(order_body)
    track = post_new_order_response.json()['track']
    sender_scooter_request.get_order_by_track(track)
    order_id = 123456
    response = sender_scooter_request.accept_order(order_id, courier_id)
    assert response.status_code == 404
    assert response.json()['message'] == 'Заказа с таким id не существует'


def test_accept_order_wrong_courier_id():
    courier_body = {
       "login": "ninja4",
       "password": "1234",
       "firstName": "saske"
    }
    sender_scooter_request.post_create_courier(courier_body)
    courier_login = {
       "login": "ninja4",
       "password": "1234"
    }
    sender_scooter_request.post_courier_login(courier_login)
    courier_id = 123456
    order_body = data.order_body
    post_new_order_response = sender_scooter_request.new_order(order_body)
    track = post_new_order_response.json()['track']
    get_order_by_track_response = sender_scooter_request.get_order_by_track(track)
    order_id = get_order_by_track_response.json()['order']['id']
    response = sender_scooter_request.accept_order(order_id, courier_id)
    assert response.status_code == 404
    assert response.json()['message'] == 'Курьера с таким id не существует'


def test_accept_order_no_courier_id():
    courier_body = {
       "login": "ninja4",
       "password": "1234",
       "firstName": "saske"
    }
    sender_scooter_request.post_create_courier(courier_body)
    courier_login = {
       "login": "ninja4",
       "password": "1234"
    }
    sender_scooter_request.post_courier_login(courier_login)
    courier_id = ''
    order_body = data.order_body
    post_new_order_response = sender_scooter_request.new_order(order_body)
    track = post_new_order_response.json()['track']
    get_order_by_track_response = sender_scooter_request.get_order_by_track(track)
    order_id = get_order_by_track_response.json()['order']['id']
    response = sender_scooter_request.accept_order(order_id, courier_id)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для поиска'