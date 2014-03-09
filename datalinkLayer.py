import physicalLayer

class DatalinkLayer:
    def __init__(self):
        self.physicalLayer = physicalLayer.PhysicalLayer()

    def transfer(self, data):
        self.physicalLayer.transfer(data)

    def receive(self):
        return self.physicalLayer.receive()
