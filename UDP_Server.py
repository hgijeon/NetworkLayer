import newSocket as socketLib
import time
import datetime
#import Users

class UDP_Server(object):
    
    def __init__(self,IP=socketLib.findByDomain("T3"),port=80):
        while True:
            self.run_the_chat(IP,port)

    def run_the_chat(self,IP,port):
        socket, AF_INET, SOCK_DGRAM, timeout = socketLib.socket, socketLib.AF_INET, socketLib.SOCK_DGRAM, socketLib.timeout
        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.bind((IP,port))
            sock.settimeout(2.0) # 2 second timeout
            Users={}
            MsgList=[] #List of all messages on server
            AdminList={} #List of Admins (added 2/25/2014} Stores Address and T/F
            BannedList={} #Store Address and T/F
            Times={} #Stores index for each message based on timestamp
            password='admin' #Current Admin password
            MsgCount=0 #Index of most recent message on server
            msgHelp='/admin {password} '+ '/adminInfo '+ '/help '+'/logoff ' #List of Client Commands
            msgAdminHelp='/ban {user}' #List of Admin Commands
            print ("UDP Server started on IP Address {}, port {}".format(IP,port))

            while True:
                try:
                    bytearray_msg, address = sock.recvfrom(1024)
                    source_IP, source_port = address
                    
                    ts=time.time()
                    st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    
                    test=address in Users #Returns True is user is logged on to the server, False if not
                    if test==False: #Requests user to logon for the first time
                        Users[address]=st
                        MsgList+=['']
                        Times[st]=MsgCount
                        MsgCount+=1
                        bytearray_message = bytearray('Your IP and port have been added to the system!  Congratulations!' ,encoding="UTF-8")
                        bytes_sent = sock.sendto(bytearray_message, address)
                    elif test==True:
                        if source_IP not in BannedList:
                            print ("\nMessage received from IP address {}, port {}:".format(
                                source_IP,source_port))

                            if (bytearray_msg.decode("UTF-8"))[0] == '/':#Tests to see if the message starts with a / and is therefore a command
                                command = bytearray_msg.decode("UTF-8")
                                print (source_IP+': '+command)
                                if command == "/help": #Tests for /help command
                                    bytearray_message = bytearray("List of avaliable commands are: "+msgHelp,encoding="UTF-8")
                                    bytes_sent = sock.sendto(bytearray_message, address)
                                    
                                    #New command checks added (2/25/2014)
                                    #Note - commands need to be checked (sorry!)
                                        
                                elif command == "/adminInfo":
                                    if AdminList[address]:
                                        bytearray_message = bytearray("As Admin, You can use: "+msgAdminHelp+msgHelp  ,encoding="UTF-8")                                        
                                    else:
                                        bytearray_message = bytearray("If you are an admin, type /admin [password] to logon",encoding="UTF-8")
                                    bytes_sent = sock.sendto(bytearray_message, address)
                                elif command[:6] == "/admin":
                                    if command == "/admin "+password: #Tests is Admin password is provided
                                        bytearray_message = bytearray("You are now Admin!",encoding="UTF-8")
                                        bytes_sent = sock.sendto(bytearray_message, address)
                                        AdminList[address] = True #Adds user to Admin list
                                    else: #Triggers if wrong/no password is provided
                                        bytearray_message = bytearray("Admin permissions require the correct password to logon!",encoding="UTF-8")
                                        bytes_sent = sock.sendto(bytearray_message, address)
                                elif command == "/logoff":
                                    bytearray_message = bytearray("BYE - you will now be logged off",encoding="UTF-8")
                                    bytes_sent = sock.sendto(bytearray_message, address)
                                    break
                                elif "/ban" in command:
                                    print (AdminList)
                                    if address in AdminList:
                                        who = command[5:]
                                        print (who)
                                        BannedList[who] = True
                                        bytearray_message = bytearray("Your ban on "+who+" is now active",encoding="UTF-8")
                                        bytes_sent = sock.sendto(bytearray_message, address)
                                    else:
                                        bytearray_message = bytearray("You must be Admin to use this command.",encoding="UTF-8")
                                        bytes_sent = sock.sendto(bytearray_message, address)
                                        
                                else:
                                    bytearray_message = bytearray("The command you entered is not recognized.",encoding="UTF-8")
                                    bytes_sent = sock.sendto(bytearray_message, address)

                            ##Code below this point has not been modified at all
                        
                            else:
                                LastMsg=Users[address] #Reads the last message index provided by the Server to the Client since logon
                                str_message =[source_IP+': '+(bytearray_msg.decode("UTF-8"))]
                                print(str_message) #Prints the message out to the server
                            
                                Times[st]=MsgCount #Uses timestamp to access current message index
                                MsgList+=str_message #Adds latest message to the list of all messages sinse server startup
                            
                                for i in range(Times[LastMsg]+1,Times[st]+1): #Transmitts all messages from last message index to current message index.
                                    bytearray_message = bytearray(MsgList[i],encoding="UTF-8") #Back-Translate into UTF-8
                                    bytes_sent = sock.sendto(bytearray_message, address) #Transmit message

                                MsgCount+=1

                                Users[address]=st
                                
                        ##Added with ban Code
                        else:
                            bytearray_message=bytearray("You are on the 'banned' list - Contact an Admin to have the ban lifted",encoding="UTF-8")
                            bytes_sent = sock.sendto(bytearray_message, address)
                            
                        ##Nothing changed below
        
                except timeout: ## Handles timeout with the server.
                    print("")
                    continue
                
                
            



            
        
