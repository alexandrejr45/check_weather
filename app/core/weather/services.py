from . import api


def get_current_weather(params):
    try:
        response = api.get_current_weather(params)

        if response.status_code != 200:
            return response.json()

        return response.json()
    except Exception as err:
        return err
