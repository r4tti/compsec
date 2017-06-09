from debug import *
from zoodb import *
import rpclib

def transfer(sender, recipient, zoobars, token):
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('transfer', sender=sender, recipient=recipient, zoobars=zoobars, token=token)

def balance(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('balance', username=username)

def get_log(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        return c.call('get_log', username=username)
