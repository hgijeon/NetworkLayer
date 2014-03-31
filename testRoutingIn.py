import standardSocket as socketLib

lanIP = 'T'

routerDict = {
    "E":("192.168.100.50",80),
    "I":("192.168.100.73",73),
    "T":("192.168.100.84",84)
}



socket, AF_INET, SOCK_DGRAM, timeout = socketLib.socket, socketLib.AF_INET, socketLib.SOCK_DGRAM, socketLib.timeout

def sendMsg(msg):
    with socket(AF_INET, SOCK_DGRAM) as sock:
        sock.sendto(bytearray(msg.upper(),"UTF-8"), ("127.0.0.1", routerDict[lanIP][1]))

if __name__ == "__main__":
    sendMsg("T3EEE04BAHI")
