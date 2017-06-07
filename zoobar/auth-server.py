#!/usr/bin/python

import rpclib
import sys
import auth
from debug import *

class AuthRpcServer(rpclib.RpcServer):
    def rpc_login(self, user, pw):
	return auth.login(user, pw)
    
    def rpc_register(self, user, pw):
        return auth.register(user,pw)

    def rpc_check_token(self, user, token): 
        ret = auth.check_token(user, token)
        return ret

(_, dummy_zookld_fd, sockpath) = sys.argv

s = AuthRpcServer()
s.run_sockpath_fork(sockpath)
