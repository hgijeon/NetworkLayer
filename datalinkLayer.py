import physicalLayer
import timeAlarm
import time
from threading import Thread as thread


class DatalinkLayer:
    def __init__(self):
        self.macAddr = ""
        self.timeLimit = 1000000
        self.receiveQueue = []
        self.transferQueue = []
        self.lowerLayer = physicalLayer.PhysicalLayer()

        
        self.tr = True
        self.re = True
        trTh = thread(target=self.transferTh)
        reTh = thread(target=self.receiveTh)
        trTh.start()
        reTh.start()

    
    def __enter__(self):
        return self

    def cleanUp(self):
        self.tr = False
        self.re = False

            
    def settimeout(self, time):
        self.timeLimit = time

    def transferTh(self):
        while self.tr:
            if len(self.transferQueue) > 0:
                self.lowerLayer.transfer(self.transferQueue.pop(0))
            time.sleep(0.3)

    def transfer(self, data):
        self.transferQueue.append(data)


    def receive(self):
        startTime = time.time()

        while True:
            if len(self.receiveQueue)>0:
                return self.receiveQueue.pop(0)
            time.sleep(0.2)
            if time.time() - startTime > self.timeLimit:
                if self.lowerLayer.idle:
                    raise timeAlarm.TimeException()
                    n=len(self.lowerLayer.log)
                    break

		#one more chance
        startTime = time.time()

        while True:
            if len(self.receiveQueue)>0:
                return self.receiveQueue.pop(0)
            time.sleep(0.2)
            if len(self.lowerLayer) > n:
                raise timeAlarm.Timeout()

    def receiveTh(self):
        while self.re:
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
