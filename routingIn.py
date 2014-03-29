import physicalLayer
import standardSocket as socketLib

lanIP = 'T'

routerDict = {
    "E":("192.168.100.50",80),
    "I":("192.168.100.73",73),
    "T":("192.168.100.84",84)
}




lowerLayer = physicalLayer.PhysicalLayer()

socket, AF_INET, SOCK_DGRAM, timeout = socketLib.socket, socketLib.AF_INET, socketLib.SOCK_DGRAM, socketLib.timeout

with socket(AF_INET, SOCK_DGRAM) as sock:
    sock.bind(routerDict["T"])
    sock.settimeout(2.0) # 2 second timeout

    while True:
        try:
            ret, address = sock.recvfrom(1024)
                
            print("router got: "+str(ret))
            dstIP = ret[0]
            if dstIP == lanIP:
                print("sending to inside...")
                lowerLayer.transfer(ret)

        except timeout:
            print (".",end="",flush=True)
            continue
