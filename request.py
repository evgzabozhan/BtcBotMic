import requests
import Authentication


def create_session(publicKey, secretKey):
    connect = requests.session()
    connect.auth = Authentication.HS256(publicKey, secretKey)
    return connect


def get_streaming_market_data(session):
    print(session.get("https://api.hitbtc.com/api/2/trading/balance").json())


def get_streaming_trading():
    pass


def get_streaming_account():
    pass


def hitbtc_rest():
    pass
