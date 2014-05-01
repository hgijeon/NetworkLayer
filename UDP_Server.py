import newSocket as socketLib
import time
import datetime
#import Users

class UDP_Server(object):
    
    def __init__(self,IP=socketLib.findByDomain("T2"),port=80):
        while True:
            self.run_the_chat(IP,port)
            

    def run_the_chat(self,IP,port):
        socket, AF_INET, SOCK_DGRAM, timeout = socketLib.socket, socketLib.AF_INET, socketLib.SOCK_DGRAM, socketLib.timeout
        with socket(AF_INET, SOCK_DGRAM) as self.sock:
            self.sock.bind((IP,port))
            self.sock.settimeout(2.0) # 2 second timeout
            self.Users={}
            self.MsgList=[] #List of all messages on server
            self.AdminList={} #List of Admins (added 2/25/2014} Stores Address and T/F
            self.BannedList={} #Store Address and T/F
            self.Times={} #Stores index for each message based on timestamp
            password='admin' #Current Admin password
            self.MsgCount=0 #Index of most recent message on server
            self.msgHelp='/admin {password} '+ '/adminInfo '+ '/help '+'/logoff ' #List of Client Commands
            self.msgAdminHelp='/ban {user}' #List of Admin Commands
            print ("UDP Server started on IP Address {}, port {}".format(IP,port))
            self.logon=True
            self.allOtherMsg=[]

            while self.logon:
                try:
                    print('hit try')
                    if self.allOtherMsg != []:
                        print('passed through if')
                        for i in range(len(allOtherMsg)):
                            self.decodeMsg(allOtherMsg[i])
                            time.sleep(.1)
                        
                    else:
                        print('hit else')
                        bytearray_msg, address = self.sock.recvfrom(1024)
                        print('gotmsg')
                        self.decodeMsg(bytearray_msg, address)
                        print('decoded')
                        time.sleep(.1)
        
                except Exception as e: ## Handles timeout with the server
                    time.sleep(.1)
                    print (e)
                    continue
                
    def decodeMsg(self, bytearray_msg, address):
        source_IP, source_port = address
        ts=time.time()
        st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        test=address in self.Users #Returns True is user is logged on to the server, False if not
        if test==False: #Requests user to logon for the first time
            self.Users[address]=st
            self.MsgList+=['']
            self.Times[st]=self.MsgCount
            self.MsgCount+=1
            bytearray_message = bytearray('Your IP and port have been added to the system!  Congratulations!' ,encoding="UTF-8")
            bytes_sent = self.sock.sendto(bytearray_message, address)
##            self.waitForAck(Oaddress=address,OMsg=bytearray_message)
        elif test==True:
            if source_IP not in self.BannedList:
                print ("\nMessage received from IP address {}, port {}:".format(
                    source_IP,source_port))

                if (bytearray_msg.decode("UTF-8"))[0] == '/':#Tests to see if the message starts with a / and is therefore a command
                    command = bytearray_msg.decode("UTF-8")
                    print (source_IP+': '+command)
                    if command == "/help": #Tests for /help command
                        bytearray_message = bytearray("List of avaliable commands are: "+self.msgHelp,encoding="UTF-8")
                        bytes_sent = self.sock.sendto(bytearray_message, address)
##                        self.waitForAck(Oaddress=address,OMsg=bytearray_message)
                        #New command checks added (2/25/2014)
                        #Note - commands need to be checked (sorry!)
                            
                    elif command == "/adminInfo":
                        if self.AdminList[address]:
                            bytearray_message = bytearray("As Admin, You can use: "+self.msgAdminHelp+self.msgHelp  ,encoding="UTF-8")                                        
                        else:
                            bytearray_message = bytearray("If you are an admin, type /admin [password] to logon",encoding="UTF-8")
                        bytes_sent = self.sock.sendto(bytearray_message, address)
##                        self.waitForAck(Oaddress=address,OMsg=bytearray_message)
                    elif command[:6] == "/admin":
                        if command == "/admin "+password: #Tests is Admin password is provided
                            bytearray_message = bytearray("You are now Admin!",encoding="UTF-8")
                            bytes_sent = self.sock.sendto(bytearray_message, address)
                            self.AdminList[address] = True #Adds user to Admin list
                        else: #Triggers if wrong/no password is provided
                            bytearray_message = bytearray("Admin permissions require the correct password to logon!",encoding="UTF-8")
                            bytes_sent = self.sock.sendto(bytearray_message, address)
##                            self.waitForAck(Oaddress=address,OMsg=bytearray_message)
                    elif command == "/logoff":
                        bytearray_message = bytearray("BYE - you will now be logged off",encoding="UTF-8")
                        bytes_sent = self.sock.sendto(bytearray_message, address)
                        self.logon=False
                    elif "/ban" in command:
                        print (self.AdminList)
                        if address in AdminList:
                            who = command[5:]
                            print (who)
                            self.BannedList[who] = True
                            bytearray_message = bytearray("Your ban on "+who+" is now active",encoding="UTF-8")
                            bytes_sent = self.sock.sendto(bytearray_message, address)
##                            self.waitForAck(Oaddress=address,OMsg=bytearray_message)
                        else:
                            bytearray_message = bytearray("You must be Admin to use this command.",encoding="UTF-8")
                            bytes_sent = self.sock.sendto(bytearray_message, address)
##                            self.waitForAck(Oaddress=address,OMsg=bytearray_message)
                            
                    else:
                        bytearray_message = bytearray("The command you entered is not recognized.",encoding="UTF-8")
                        bytes_sent = self.sock.sendto(bytearray_message, address)
##                        self.waitForAck(Oaddress=address,OMsg=bytearray_message)

                ##Code below this point has not been modified at all
            
                else:
                    self.LastMsg=self.Users[address] #Reads the last message index provided by the Server to the Client since logon
                    str_message =[source_IP+': '+(bytearray_msg.decode("UTF-8"))]
                    print(str_message) #Prints the message out to the server
                
                    self.Times[st]=self.MsgCount #Uses timestamp to access current message index
                    self.MsgList+=str_message #Adds latest message to the list of all messages sinse server startup
                
                    for i in range(self.Times[self.LastMsg]+1,self.Times[st]+1): #Transmitts all messages from last message index to current message index.
                        bytearray_message = bytearray(self.MsgList[i],encoding="UTF-8") #Back-Translate into UTF-8
                        bytes_sent = self.sock.sendto(bytearray_message, address) #Transmit message

                    self.MsgCount+=1

                    self.Users[address]=st
                    
            ##Added with ban Code
            else:
                bytearray_message=bytearray("You are on the 'banned' list - Contact an Admin to have the ban lifted",encoding="UTF-8")
                bytes_sent = self.sock.sendto(bytearray_message, address)
##                self.waitForAck(Oaddress=address,OMsg=bytearray_message)
                            
                        ##Nothing changed below


    def waitForAck(self,Oaddress,timeout=10,OMsg=''):
        finaltime=time.time()+timeout
        while noAck:
            try:
                if time.time()>finaltime:
                    bytes_sent = sock.sendto(oMsg, Oaddress)
                else:
                    bytearray_msg, address = sock.recvfrom(1024)
                    source_IP, source_port = address
                    if address == Oaddress:
                        if 'ACK' == bytearray_msg.decode("UTF-8"):
                            noAck=False
                        else:
                            self.allOtherMsg.append(bytearray_msg.decode("UTF-8"),address)
                    else:
                        self.allOtherMsg.append(bytearray_msg.decode("UTF-8"),address)

            except Exception:
                continue
               
if __name__ == "__main__":
    print("udp server will start in 3 seconds")
    time.sleep(3)
    UDP_Server()

