import newSocket as socketLib

class CN_Echo_Server(object):
    

    
    def __init__(self,IP=socketLib.findByDomain("T1"),port=80):

        socket, AF_INET, SOCK_DGRAM, timeout = socketLib.socket, socketLib.AF_INET, socketLib.SOCK_DGRAM, socketLib.timeout
        
        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.bind((IP,port))
            sock.settimeout(2.0) # 2 second timeout
            
            print ("UDP Server started on IP Address {}, port {}".format(IP,port))
            
            while True:
                try:
                    bytearray_msg, address = sock.recvfrom(1024)
                    source_IP, source_port = address
                    
                    print ("\n{} byte message received from ip address {}, port {}:".format(len(bytearray_msg),source_IP,source_port))
                    print ("\n"+bytearray_msg.decode("UTF-8"))

                    lenx= sock.sendto(bytearray_msg, address)
                    print ("\n{} byte message echoed")
        

                except timeout:
                    print (".",end="",flush=True)
                    continue
                
if __name__ == '__main__':
    CN_Echo_Server()            



            
        
