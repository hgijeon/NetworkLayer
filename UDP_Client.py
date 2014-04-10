
import newSocket as socketLib
import physicalLayer
import timeAlarm
import time
import random
            
class UDP_Client(object):
    """UDP Client""" 
    #This worked fine when communicating within a PI (have both server and client running on the same pi)
    #04/10/2014 12:54AM - Not sure why it got buggy when we were using two PIs - may need to test this again 
    
    def __init__(self,Server_Address=(socketLib.findByDomain("T2"),80)):
        self.lowerLayer = physicalLayer.PhysicalLayer()
        self.timeLimit=4
        myAddress = (socketLib.findByDomain("T2"),84)

        socket, AF_INET, SOCK_DGRAM, self.timeout = socketLib.socket, socketLib.AF_INET, socketLib.SOCK_DGRAM, socketLib.timeout

        self.Server_Address = Server_Address
        with socket(AF_INET,SOCK_DGRAM) as self.sock:
            self.sock.bind(myAddress)
            self.sock.settimeout(2) # 1 second timeout
            
            print ("UDP_Client started for UDP_Server at IP address {} on port {}".format(
                self.Server_Address[0],self.Server_Address[1]))

            # Auto sending first message
            self.sendStrMessage("Hello Server!")
            # Recieve response
            self.receiveMessage()

    
            while True:
                
                str_message = input("Enter message to send to server: ")#User input message

                if not str_message:
                    break

                self.sendStrMessage(str_message)
                self.notRecieved=True
                i=1
                self.receiveMessage()
                '''
                while self.notRecieved:
                    time.sleep(random.randint(0,5+i))
                    self.sendStrMessage(str_message)
                    self.receiveMessage()
                    i+=2
                    '''

        print("UDP_Client ended")
        
    def sendStrMessage(self, message):#Translates message from string to UTF-8 and transmitts
        bytearray_message = bytearray(message,encoding="UTF-8")#Translate
        bytes_sent = self.sock.sendto(bytearray_message, self.Server_Address)#Transmit
        # print ("{} bytes sent".format(bytes_sent))
    
    
    def receiveMessage(self):
        while True:
            with timeAlarm.Timeout(self.timeLimit):
                try:
                    #Attempts to recieve the return message from the server
                    bytearray_msg, address = self.sock.recvfrom(1024)
                    source_IP, source_port = address
                    print(self.decodeMessage(bytearray_msg.decode("UTF-8")))
                    self.notRecieved=False
                
                except timeAlarm.TimeException:
                    if self.lowerLayer.idle:
                        break
                """
            except self.timeout:
                if self.lowerLayer.idle:
                    break #After timeout, returns client to user for next input
               """

    def decodeMessage(self, string):
        return self.Message(string)
    
    class Message:
        def __init__(self, message = ""):
            self.message = message
        
        def __str__(self):
            return self.message
