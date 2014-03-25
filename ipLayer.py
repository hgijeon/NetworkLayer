import datalinkLayer

class IpLayer:
    def __init__(self):
        self.lowerLayer = datalinkLayer.DatalinkLayer()

    def transfer(self, data):
        self.lowerLayer.transfer(data)
        

    def receive(self):
        self.lowerLayer.receive()

    def setMacAddr(self, macAddr):
        self.lowerLayer.setMacAddr(macAddr)
