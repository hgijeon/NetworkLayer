import physicalLayer

class DatalinkLayer:
    def __init__(self):
        self.macAddr = ""
        self.lowerLayer = physicalLayer.PhysicalLayer()

    def transfer(self, data):
        self.lowerLayer.transfer(data)

    def receive(self):
        while True:
            ret = self.lowerLayer.receiveResistor()
            if ret != None:
                print("datalinkLayer got: "+ret)
                if ret[:2] == self.macAddr:
                    return ret

    def setMacAddr(self, macAddr):
        self.macAddr = macAddr
        print("MACaddr: "+self.macAddr)
