T_ROUTER_IP = '0.0.T.13'
import socket
class Router:
    def __init__(self):
        self.routerIP = T_ROUTER_IP
        
    def reroute_msg(self,address,msg):
        self.myIP = address[1]
        self.myMAC = self.myIP.split('.')[2]
        self.dstLAN = '192.168.100.'+ self.myMAC
        self.msg = msg
        socket.socket.send_to(self,self.dstLAN,self.msg)
