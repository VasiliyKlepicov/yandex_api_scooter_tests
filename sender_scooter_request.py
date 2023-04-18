import configuration
import requests


def ping_server():
    return requests.get(configuration.URL + configuration.PING_SERVER)


def new_order(order_body):
    return requests.post(configuration.URL + configuration.NEW_ORDER_PATH,
                         json=order_body)


def get_order_by_track(track):
    return requests.get(configuration.URL + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={'t': track})


def get_all_orders():
    return requests.get(configuration.URL + configuration.GET_ORDERS_PATH)


def get_orders_courier_id(courier_id):
    return requests.get(configuration.URL + configuration.GET_ORDERS_PATH,
                        params={'courierId': courier_id})


def cancel_order(track):
    return requests.put(configuration.URL + configuration.CANCEL_ORDER_PATH,
                        params={'track': track})


def create_courier(courier_body):
    return requests.post(configuration.URL + configuration.CREATE_COURIER_PATH,
                         json=courier_body)


def post_courier_login(courier_login):
    return requests.post(configuration.URL + configuration.COURIER_LOGIN_PATH,
                         json=courier_login)


def accept_order(order_id, courier_id):
    return requests.put(configuration.URL + configuration.ACCEPT_ORDER_PATH
                        + str(order_id), params={'courierId': courier_id})


def finish_order(order_id):
    return requests.put(configuration.URL + configuration.FINISH_ORDER_PATH
                        + str(order_id))


def delete_courier(courier_id):
    return requests.delete(configuration.URL + configuration.DELETE_COURIER_PATH
                           + str(courier_id))


def stations_search(station):
    return requests.get(configuration.URL + configuration.STATION_SEARCH,
                        params={'s': station})
