import physicalLayer
import timeAlarm


class DatalinkLayer:
    def __init__(self):
        self.macAddr = ""
        self.timeLimit = 0
        self.lowerLayer = physicalLayer.PhysicalLayer()

    def transfer(self, data):
        self.lowerLayer.transfer(data)

    def receive(self):
        while True:
            with timeAlarm.Timeout(self.timeLimit):
                try:
                    while True:
                        ret = self.lowerLayer.receiveResistor()
                        if ret != None:
                            print("datalinkLayer got: "+ret)
                            if ret[1] == self.macAddr:
                                return ret
                except timeAlarm.TimeException:
                    print("timeException")


    def setMacAddr(self, macAddr):
        self.macAddr = macAddr
        print("MACaddr: "+self.macAddr)

    def settimeout(self, limit):
        self.timeLimit = limit
