import queue as q
import physicalLayer
import timeAlarm
import time
from threading import Thread as thread


class DatalinkLayer:
    def __init__(self):
        self.macAddr = ""
        self.timeLimit = 1000000
        self.receiveQueue = q.Queue()
        self.transferQueue = q.Queue()
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
            if not self.transferQueue.empty():
                self.lowerLayer.transfer(self.transferQueue.get())
            time.sleep(0.3)

    def transfer(self, data):
        self.transferQueue.put(data)


    def receive(self):
        startTime = time.time()

        while True:
            return self.receiveQueue.get(1,3)
##            if not self.receiveQueue.empty():
##                return self.receiveQueue.get()
##            else:
##                if self.lowerLayer.idle:
##                    time.sleep(0.2)
##                    break
##                else:
##                    time.sleep(0.2)
##                    pass

#this is for the second chance (if physical layer is getting something.)
        """
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
        """

    def receiveTh(self):
        while self.re:
            ret = self.lowerLayer.receiveResistor()
            if ret != None:
                #print("datalinkLayer got: "+ret)
                if ret[1] == self.macAddr:
                        self.receiveQueue.put(ret)


    def setMacAddr(self, macAddr):
        self.macAddr = macAddr
        print("MACaddr: "+self.macAddr)

    def settimeout(self, limit):
        self.timeLimit = limit
