import datalinkLayer

class IpLayer:
    def __init__(self):
        self.datalinkLayer = datalinkLayer.DatalinkLayer()

    def transfer(self, srcAddr, dstAddr, data):
        srcIp, srcPort = srcAddr
        dstIp, dstPort = dstAddr

        header = str(srcIP) + str(srcPort) # TODO

        self.datalinkLayer.transfer(header + data)

    def receive(self):
        while True:
            ret = self.datalinkLayer.receive()
            if ret != None:
                srcIp = ret[0:5]
                #TODO fix
                data = ret[:]
                return ((srcIp), data)
        
