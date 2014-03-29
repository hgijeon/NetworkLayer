import newSocket
socket, AF_INET, SOCK_DGRAM = newSocket.socket, newSocket.AF_INET, newSocket.SOCK_DGRAM

with socket(AF_INET, SOCK_DGRAM) as sock:
    sock.bind(('0.0.73.68',84))

    print(sock.recvfrom(1024))
