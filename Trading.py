
def but_btc(session):
    pass


def sell_btc(session):
    pass


def get_balance(session, url):
    r = session.get(url).json()
    balance = {}
    for value in r:
        if value['currency'] == 'USD' or value['currency'] == 'BTC':
            balance[value['currency']] = f"{value['currency']}, available : {value['available']}, reserved : {value['reserved']}"
    return balance
