
import newSocket as socketLib
import physicalLayer
import timeAlarm
import time
import random
import signal
from threading import Thread as thread
import threading
            
class UDP_Client(object):
    """UDP Client""" 
    #This worked fine when communicating within a PI (have both server and client running on the same pi)
    #04/10/2014 12:54AM - Not sure why it got buggy when we were using two PIs - may need to test this again 
    
    def __init__(self,Server_Address=(socketLib.findByDomain("T2"),80)):
        self.lowerLayer = physicalLayer.PhysicalLayer()
        self.timeLimit=30
        myAddress = (socketLib.findByDomain("T2"),84)
        signal.signal(signal.SIGALRM,self.alarmHandler)
        socket, AF_INET, SOCK_DGRAM, self.timeout = socketLib.socket, socketLib.AF_INET, socketLib.SOCK_DGRAM, socketLib.timeout
        self.receivedmsg=[]

        self.Server_Address = Server_Address

##        receivingThr = thread(target=self.receiveMessage)
##        receivingThr.start()
##        lock = threading.Lock()
        
        with socket(AF_INET,SOCK_DGRAM) as self.sock:
            self.sock.bind(myAddress)
            self.sock.settimeout(10) # 10 second timeout
            
            print ("UDP_Client started for UDP_Server at IP address {} on port {}".format(
                self.Server_Address[0],self.Server_Address[1]))

            # Auto sending first message
            self.sendStrMessage("Hello Server!")
            # Recieve response
##            self.receiveMessage()

    
            while True:
##                try:

                time.sleep(2)
                timeout=time.time()+self.timeLimit
                while self.receivedmsg==[]: #and time.time()< timeout:
                    self.receiveMessage()
                    time.sleep(.1)
                for i in range(len(self.receivedmsg)):
                    print (self.receivedmsg[i])
                self.receivedmsg=[]

                self.userInput()


##                    self.receiveMessage()
##                    print('went to recive messages')

##                except Exception as e:
##                    print('reach here')
##                    print(e)
##                    self.receiveMessage()

        print("UDP_Client ended")
        
    def sendStrMessage(self, message):#Translates message from string to UTF-8 and transmitts
        bytearray_message = bytearray(message,encoding="UTF-8")#Translate
        bytes_sent = self.sock.sendto(bytearray_message, self.Server_Address)#Transmit
        # print ("{} bytes sent".format(bytes_sent))
    
    
    def receiveMessage(self):
        while True:
            try:
                #Attempts to recieve the return message from the server
                bytearray_msg, address = self.sock.recvfrom(1024)
                source_IP, source_port = address
                self.receivedmsg.append(self.decodeMessage(bytearray_msg.decode("UTF-8")))

            except Exception as e:
                time.sleep(.1)
                break

    def userInput(self):
        str_message = input("Enter message to send to server: ")#User input message

##        if not str_message:
##            break
        self.sendStrMessage(str_message)
        time.sleep(.1)
            

    def decodeMessage(self, string):
        return self.Message(string)
    
    class Message:
        def __init__(self, message = ""):
            self.message = message
        
        def __str__(self):
            return self.message

    def alarmHandler(self,signum,frame):
        raise Exception

    def inputWithTimeout(self,prompt,timeout=10):
        print('I hate this')
        signal.alarm(timeout)
        try:
            msg=input(prompt)
            print (msg)
            signal.alarm(0)
            return msg
        except Exception as e:
            print ('got to except')
            print(e)
            print ("didn't switched alarm")
##            signal.alarm(0)
            print ('raised exception')
            return ''

if __name__ == "__main__":
    print("udp client will start in 3 sec...")
    time.sleep(3)
    UDP_Client()
