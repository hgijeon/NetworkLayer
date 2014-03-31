import ledOnOff
import morse
import chargetimes
from time import sleep, time

startSeq = '-.-.-'
stopSeq = '.-.-.'

sendRate = 0.05
receiveRate = 0.000000001
calculatedUnitTime = None

class PhysicalLayer:
    def __init__(self):
        self.idle = True
        self.noiseFilter = self.NoiseFilter()
        self.startChecker = self.StartChecker()
        self.stopChecker = self.StopChecker()
        self.bitMessage = []
        self.log = []

    def transfer(self, data):
        sleep(0.3)
        self.an2led(data, sendRate)

    def receive(self):
        on = chargetimes.getLed(receiveRate)
        return self.addOne(on, time())

    def receiveResistor(self):
        on = chargetimes.getLedResistor(receiveRate)
        return self.addOne(on, time())

    def addOne(self, on, timestamp):
        
        tup = self.noiseFilter.add(on, timestamp)
        if tup != None:
            #print(tup)
            if self.idle:
                newLenOfDot = self.startChecker.addTup(tup)
                if newLenOfDot != None:
                    self.noiseFilter.dotTime = newLenOfDot
                    if self.startChecker.isStarted():
                        print("start!!")
                        self.startChecker.reset()
                        self.idle = False
            elif not self.idle:
                self.bitMessage.append(self.analysis(tup))

                if self.stopChecker.isStop(self.bitMessage):
                    self.stopChecker.removeStopSeq(self.bitMessage)
                    print("stop!!")
                    #print(self.bitMessage)
                    #print(morse.bitData2morse(self.bitMessage))
                    #print("Received Message: "+morse.morse2an(morse.bitData2morse(self.bitMessage)))
                    self.log.append(self.bitMessage)
                    self.bitMessage=[]
                    self.idle = True
                    return morse.morse2an(morse.bitData2morse(self.log[-1]))

                    
    def analysis(self, tup):
        return [tup[0], int(0.5 + tup[1]/self.noiseFilter.dotTime)]

    
    def bit2led(self, bitList, unitTime):
        for e in bitList:
            if e == '0':
                ledOnOff.off()
            elif e == '1':
                ledOnOff.on()
            sleep(unitTime)

    def an2led(self, string, unitTime = .1):
        self.bit2led(morse.morse2bit([startSeq]+morse.an2morse(string)+[stopSeq]), unitTime)
    
    class NoiseFilter:
        def __init__(self):
            self.queue = [[False,0]]
        
        def add(self, on, timestamp):
            if on == self.queue[-1][0]:
                if len(self.queue) >= 2: # and not self.isNoise(timestamp - self.queue[-1][1]):
                    ret = self.queue[0]
                    self.queue = [self.queue[1]]
                    ret[1]=self.queue[0][1] - ret[1]
                    return ret
            else:
                if len(self.queue) == 2:    # self.queue[-1] is noise
                    self.queue.pop()
                else:
                    self.queue.append([on,timestamp])
            
        def isNoise(self, timeDiff):
            if calculatedUnitTime == None:
                return timeDiff < sendRate/4
            return int(0.75 + timeDiff/calculatedTime) < 1        

    class StopChecker:
        def __init__(self):            
            self.stopSeq = stopSeq
            self.match = []
            for c in self.stopSeq:
                if c == '.':
                    self.match.append([True,1])
                elif c == '-':
                    self.match.append([True,3])
                self.match.append([False,1])
            self.match.pop()
        
        def isStop(self, bitMessage):
            if len(bitMessage) < len(self.match):
                return False
            return bitMessage[-len(self.match):] == self.match
        def removeStopSeq(self, bitMessage):
            for e in self.match:
                bitMessage.pop()
    
    class StartChecker:
        def __init__(self):
            self.startSeq = startSeq
            self.match = []
            for c in self.startSeq:
                if c == '.':
                    self.match.append([True,1])
                elif c == '-':
                    self.match.append([True,3])
                self.match.append([False,1])
            self.match.pop()
            
            self.reset()
            
        def isStarted(self):
            return self.index >= len(self.match)
            
        def reset(self):
            self.index = 0
            self.dic = {1:[], 3:[]}
        
        def addTup(self, valCount):
            if self.index == 0:
                if(valCount[0] == True):
                    self.dic[self.match[0][1]].append(valCount[1])
                    self.index += 1
                    return self.lenOfDot()
            else:
                if valCount[0] == self.match[self.index][0]:
                    roundLen = int((valCount[1]/self.lenOfDot()) + 0.5)
                    if roundLen == self.match[self.index][1]:
                        self.dic[roundLen].append(valCount[1])
                        self.index += 1
                        return self.lenOfDot()      #return lenOfDot
                self.reset()
                        
        def lenOfDot(self):
            tmp = self.dic[1] + [e / 3 for e in self.dic[3]]
            return sum(tmp) / len(tmp)
        
