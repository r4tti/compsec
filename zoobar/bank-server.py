#!/usr/bin/python

import rpclib
import sys
import bank
from debug import *
from sqlalchemy.orm import class_mapper
import auth_client

def serialize(m):
  cs = [c.key for c in class_mapper(m.__class__).columns]
  return dict((c, getattr(m, c)) for c in cs)

class BankRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, sender, recipient, zoobars, token):
	check = auth_client.check_token(sender, token)
        print(check)
        if not check:
	    return None
        return bank.transfer(sender, recipient, zoobars)

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        serialized_labels = [ serialize(label) for label in bank.get_log(username) ]
        print([label for label in serialized_labels ])
        return serialized_labels


(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
