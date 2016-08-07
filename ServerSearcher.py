import socket
import sys

SERVER_PORT = 10101


def main():
    global SERVER_PORT
    if(len(sys.argv) == 2):
        SERVER_PORT = int(sys.argv[1])
    addr = ('<broadcast>', SERVER_PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto('GetIP'.encode('utf-8'), addr)
    
    responseData, peerAddr = s.recvfrom(1024)
    responseMsg = responseData.decode('utf-8')
    print('server ip: ' + responseMsg)


if __name__ == '__main__':
    main()