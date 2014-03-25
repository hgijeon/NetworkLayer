import physicalLayer

class DatalinkLayer:
    def __init__(self):
        self.lowerLayer = physicalLayer.PhysicalLayer()

    def transfer(self, data):
        self.lowerLayer.transfer(data)

    def receive(self):
        while True:
            ret = self.lowerLayer.receive()
            if ret != None:
                print("datalinkLayer got: "+ret)
                if ret[:2] == self.macAddr
                    return ret

    def setMacAddr(self, macAddr):
        self.macAddr = macAddr
