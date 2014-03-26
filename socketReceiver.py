import newSocket
socket, AF_INET, SOCK_DGRAM = newSocket.ttsock, newSocket.AF_INET, newSocket.SOCK_DGRAM

with socket(AF_INET, SOCK_DGRAM) as sock:
    sock.bind(("TA","A"))

    print(sock.recvfrom(1024))
