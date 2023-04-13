import sender_scooter_request


def positive_assert(track):
    response = sender_scooter_request.get_order_by_track(track)
    assert response.status_code == 200


def negative_assert(track):
    response = sender_scooter_request.get_order_by_track(track)
    assert response.status_code == 404
    assert response.json()['message'] == 'Заказ не найден'


def negative_assert_no_track(track):
    response = sender_scooter_request.get_order_by_track(track)
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для поиска'


def test_1_original_track_get_success_response():
    positive_assert(sender_scooter_request.track)


def test_2_wrong_track_get_error_response():
    negative_assert(111111)


def test_3_zero_track_get_error_response():
    negative_assert(0)


def test_4_no_track_get_error_response():
    negative_assert_no_track('')
