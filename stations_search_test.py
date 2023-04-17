import sender_scooter_request


def test_stations_search():
    station = 'Сокол'
    response = sender_scooter_request.stations_search(station)
    assert response.status_code == 200
