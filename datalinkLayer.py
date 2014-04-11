import physicalLayer
import timeAlarm
import time
from threading import Thread as thread


class DatalinkLayer:
    def __init__(self):
        self.macAddr = ""
        self.timeLimit = 0
        self.receiveQueue = []
        self.transferQueue = []
        self.lowerLayer = physicalLayer.PhysicalLayer()

        thread(target=self.transferTh).start()
        thread(target=self.receiveTh).start()
        

    def transferTh(self):
        while True:
            if len(self.transferQueue) > 0:
                self.lowerLayer.transfer(self.transferQueue.pop(0))
            time.sleep(0.1)

    def transfer(self, data):
        self.transferQueue.append(data)


    def receive(self):
        with timeAlarm.Timeout(self.timeLimit):
            try:
                while True:
                    if len(self.receiveQueue)>0:
                        return self.receiveQueue.pop(0)
                    time.sleep(0.1)
            except:
                raise

    def receiveTh(self):
        while True:
            ret = self.lowerLayer.receiveResistor()
            if ret != None:
                print("datalinkLayer got: "+ret)
                if ret[1] == self.macAddr:
                        self.receiveQueue.append(ret)


    def setMacAddr(self, macAddr):
        self.macAddr = macAddr
        print("MACaddr: "+self.macAddr)

    def settimeout(self, limit):
        self.timeLimit = limit
