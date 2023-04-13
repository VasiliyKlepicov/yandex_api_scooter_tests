import configuration
import requests
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE
                         + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)


response = post_new_order()
track = response.json()['track']


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE
                        + configuration.GET_ORDER_BY_TRACK_NUMBER_PATH
                        + str(track))


response = get_order_by_track(track)
