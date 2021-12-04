import Trading
import properties
import request

settings = properties.settings

session = request.create_session(settings['public_key'], settings['secret_key'])
print(Trading.get_balance(session, f"{settings['url'] + settings['url_balance']}"))