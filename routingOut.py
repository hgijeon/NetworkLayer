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
    
    while True:
        ret=None
        while ret==None:
            ret = lowerLayer.receive()
            
        print("router got: "+ret)
        dstIP = ret[0]
        if dstIP != lanIP:
            targetRouter = routerDict[dstIP]
            print("sending to router "+dstIP+": "+targetRouter)
            sock.sendto(bytearray(ret,encoding="UTF-8"), targetRouter)

