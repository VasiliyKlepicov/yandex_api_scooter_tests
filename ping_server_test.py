import sender_scooter_request


def test_ping_server():
    response = sender_scooter_request.ping_server()
    assert response.status_code == 200
    assert response.text == 'pong;'
