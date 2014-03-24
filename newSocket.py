import socket
import ipLayer
sock = socket.socket
AF_INET = 2
SOCK_DGRAM = 2
#import class for morse code


class ttsock:
    def __init__(self,family,type):
	self.IpLayer = ipLayer.IpLayer()
        #CHECK FOR
        if(family == AF_INET) and (type == SOCK_DGRAM):
            return
        else:
            print("nope = address and type do not match")
    
    def bind(self,address):
	self.myaddress = address
        self.myipaddress = address[0]
        self.myport  = address[1]
        return
    
    def send_to(self,address,msg):

        ip = self.address[0]
        to_ip = address[0]
        if ip[2]==to_ip[2]:
            self.IpLayer.transfer(self.myaddress,address,msg)
        else:
            address[0]='192.168.100.',to_ip[2]
            self.IpLayer.transfer(self.myaddress,address,msg)

	#self.toipaddress = address[0]
        #self.toport = address[1]
        #self.msg = msg
        #add more to this
    
    def receive_from(self,max_length):
        #add max_length stuff to this later
	self.IpLayer.receive()

        #function to route from "router socket" to CN Socket {pass in all ip stuff as a message
	as the argString
    
#this is essentially the echo router (team socket as opposed to the interLANs socket)
