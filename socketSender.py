import newSocket
socket, AF_INET, SOCK_DGRAM = newSocket.socket, newSocket.AF_INET, newSocket.SOCK_DGRAM

with socket(AF_INET, SOCK_DGRAM) as sock:
    sock.bind(("0.0.84.50",84))

    sock.sendto("SOS",("0.0.73.68",69))
