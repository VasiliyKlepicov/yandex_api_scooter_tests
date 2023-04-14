import configuration
import requests


def post_new_order(order_body):
    return requests.post(configuration.URL
                         + configuration.CREATE_ORDER_PATH,
                         json=order_body)


def get_order_by_track(track):
    return requests.get(configuration.URL
                        + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={'t': track})
