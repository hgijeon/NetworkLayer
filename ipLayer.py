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
                dstIp = ret[0]+ret[1]
                srcIp  = ret[2]+ret[3]
		dstPort = ret[7]
		srcPort = ret[8]

		#numbering based off of CompNet StandardIPUDP pdf with the bases and whatnot
                data = ret[9:]
                return ((srcIp,srcPort),data)
    
