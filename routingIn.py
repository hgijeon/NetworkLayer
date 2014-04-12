import physicalLayer
import standardSocket as socketLib

lanIP = 'T'

routerDict = {
    "E":("192.168.100.50",5080),
    "I":("192.168.100.73",5073),
    "T":("192.168.100.84",5084)
}




lowerLayer = physicalLayer.PhysicalLayer()

socket, AF_INET, SOCK_DGRAM, timeout = socketLib.socket, socketLib.AF_INET, socketLib.SOCK_DGRAM, socketLib.timeout

with socket(AF_INET, SOCK_DGRAM) as sock:
    sock.bind(routerDict["T"])
    print("'routing in' is now running....")

    while True:
        try:
            ret, address = sock.recvfrom(1024)
            ret = ret.decode("UTF-8")                

            print("router got: "+str(ret))
            dstIP = ret[0]
            if dstIP == lanIP:
                print("sending to inside...")
                lowerLayer.transfer(ret)
        except timeout:
            print (".",end="")
            continue
