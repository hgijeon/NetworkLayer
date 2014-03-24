import socket
import ipLayer
sock = socket.socket
socket.AF_INET
socket.SOCK_DGRAM
#import class for morse code


class ttsock:
    def __init__(self, family,type):
	self.IpLayer = ipLayer.IpLayer()
        #CHECK FOR 2,2
        if(family == 2) and (type == 2):
            return
        else:
            print("nope")
    
    def bind(self,address):
	self.myaddress = address
        self.myipaddress = address[0]
        self.myport  = address[1]
        return
    
    def send_to(self,address,msg):
	self.IpLayer.transfer(self.myaddress,address,msg)

	#self.toipaddress = address[0]
        #self.toport = address[1]
        #self.msg = msg
        #add more to this
    
    def receive_from(self,max_length):
        #add max_length stuff to this later
	self.IpLayer.receive()

        
    
