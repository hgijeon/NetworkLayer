import ipLayer
import timeAlarm

AF_INET = 2
SOCK_DGRAM = 2

base36 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def tobase36str(n):
    return base36[n//36] + base36[n%36]

timeout = timeAlarm.TimeException 
portDict = {
    69:'E',
    84:'A',
    80:'B'
}
revPortDict = {v:k for (k,v) in portDict.items()}

ipDict = {
    '0.0.73.68':'ID',
    '0.0.73.78':'IN',
    '0.0.73.73':'II',
    '0.0.84.50':'T1',
    '0.0.73.82':'IR',
    '0.0.69.84':'ET',
    '0.0.69.69':'EE',
    '0.0.84.52':'T3',
    '0.0.69.73':'EI',
    '0.0.69.83':'ES',
    '0.0.84.51':'T2'
}
revIpDict = {v:k for (k,v) in ipDict.items()}

def findByDomain(name):
    return revIpDict[name]


class socket:
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        self.lowerLayer.cleanUp()
        pass
        
    def __init__(self,family,type):
        #CHECK FOR
        if(family == AF_INET) and (type == SOCK_DGRAM):
            self.ip_protocolCode = 'E'
            self.lowerLayer = ipLayer.IpLayer()
            return
        else:
            print("nope = address and type do not match")
    

    def settimeout(self,time):
        self.lowerLayer.settimeout(time)

    def bind(self,address):
        address = (ipDict[address[0]], portDict[address[1]])
        self.myaddress = address
        self.myipaddress = address[0]
        self.myport  = address[1]
        print("ip: "+self.myipaddress+"\tport: "+self.myport)

        self.lowerLayer.setMacAddr(self.myipaddress[1])
        return
    
    def sendto(self,msg,address):
        if isinstance(msg, bytearray):
            msg=msg.decode("UTF-8")

        address = (ipDict[address[0]], portDict[address[1]])
        udp_header = address[1] + self.myport
        udp_packet = udp_header + msg
        
        ip_header = address[0] + self.myipaddress + self.ip_protocolCode + tobase36str(len(udp_packet))
        ip_packet = ip_header + udp_packet
        
        self.lowerLayer.transfer(ip_packet)
        return len(msg)
        
    
    def recvfrom(self,max_length):
        #add max_length stuff to this later
        while True:
            ip_packet = self.lowerLayer.receive()
            
            ip_dstAddr = ip_packet[0:2]
            ip_srcAddr = ip_packet[2:4]
            ip_protocolCode = ip_packet[4]
            print("dstIP: "+ip_dstAddr+"\tsrcIP: "+ip_srcAddr+"\tprotocol: "+ip_protocolCode)
            
            if(ip_dstAddr == self.myipaddress) and (ip_protocolCode == self.ip_protocolCode):
                udp_packet = ip_packet[7:]

                udp_dstPort = udp_packet[0]
                udp_srcPort = udp_packet[1]
                print("dstPort: "+udp_dstPort+"\tsrcPort: "+udp_srcPort)

                if udp_dstPort == self.myport:
                    msg = udp_packet[2:]
                    print("msg: "+msg)
                    
                    return (bytearray(msg,encoding="UTF-8"), (revIpDict[ip_srcAddr], revPortDict[udp_srcPort]))
