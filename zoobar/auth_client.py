from debug import *
from zoodb import *
import rpclib

def login(username, password):
    with rpclib.client_connect('/authsvc/sock') as c:
        ret = c.call('login', user=username, pw=password)
        return ret

def register(username, password):
    with rpclib.client_connect('/authsvc/sock') as c:
        return c.call('register', user=username, pw=password)

def check_token(username, token):
    with rpclib.client_connect('/authsvc/sock') as c:
        return c.call('check_token', user=username, token=token)
