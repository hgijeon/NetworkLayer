import socket
import ipLayer
sock = socket.socket
AF_INET = 2
SOCK_DGRAM = 2
#import class for morse code

base36 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def tobase36str(n):
    return base36[n//36] + base36[n%36]
    

class ttsock:
    def __init__(self,family,type):
        #CHECK FOR
        if(family == AF_INET) and (type == SOCK_DGRAM):
            self.ip_protocolCode = 'E'
            self.lowerLayer = ipLayer.IpLayer()
            return
        else:
            print("nope = address and type do not match")
    
    def bind(self,address):
	self.myaddress = address
        self.myipaddress = address[0]
        self.myport  = address[1]

        self.lowerLayer.setMacAddr(self.myipaddress)
        return
    
    def send_to(self,address,msg):
        udp_header = address[1] + self.myport
        udp_packet = udp_header + msg
        
        ip_header = address[0] + self.myipaddress + ip_protocolCode + tobase36str(len(udp_packet))
        ip_packet = ip_header + udp_packet
        
        self.lowerLayer.transfer(ip_packet)
        
    
    def recvfrom(self,max_length):
        #add max_length stuff to this later
        while True:
            ip_packet = self.lowerLayer.receive()
            
            ip_dstAddr = packet[0:2]
            ip_srcAddr = packet[2:4]
            ip_protocolCode = packet[4]
            
            if(ip_dstAddr == self.myipaddress) and (ip_protocolCode == self.ip_protocolCode):
                udp_packet = ip_packet[7:]

                udp_dstPort = udp_packet[0]
                udp_srcPort = udp_packet[1]

                if udp_dstPort == self.myport:
                    msg = udp_packet[2:]
                    
                    return (msg, (ip_srcAddr, udp_srcPort) 


        #function to route from "router socket" to CN Socket {pass in all ip stuff as a message as the argString

    
#this is essentially the echo router (team socket as opposed to the interLANs socket)
