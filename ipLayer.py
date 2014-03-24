import datalinkLayer

class IpLayer:
    def __init__(self):
        self.datalinkLayer = datalinkLayer.DatalinkLayer()

    def transfer(self, srcAddr, dstAddr, data):
        srcIp, srcPort = srcAddr
        dstIp, dstPort = dstAddr

        header = str(dstIP) + str(srcIp) + str(dstPort) + str(srcPort)
        #LAN Transmission
        #startcode + MAC Header (determined by team) + IP Header + UDP Packet + endcode
        #new IP header needs destination IP address + Source IP + protocol code + length of payload
        #UDP needs destinationport + sourceport +   msg
        self.datalinkLayer.transfer(header + data)

    def receive(self):
        while True:
            ret = self.datalinkLayer.receive()
            if ret != None:
                srcIp = ret[1]
		srcPort = ret[3]
		dstIp = ret[0]
		dstPort = ret[2]

                data = ret[4:]
                return ((srcIp,srcPort),data)
    
