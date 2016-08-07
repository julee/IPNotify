import socket
import time
import json
import os
import netifaces

config = ''

def getIfaceIP(name):
    return netifaces.ifaddresses(name)[2][0]['addr']


def processMessage(s, clientAddr, msg):
    global config
    if(msg == 'GetIP'):
        ip = getIfaceIP(config['net_iface_name'])
        response = \
        { 'msg': msg, 
          'response': 
          {
              'host_name': config['host_name'],
              'ip': ip
          }
        }
        responseData = json.dumps(response).encode('utf-8')
        
        time.sleep(0.01)
        for i in range(10):
            s.sendto(responseData, clientAddr)
            time.sleep(0.1)


def main():
    global config
    configFile = os.path.dirname(os.path.abspath(__file__)) + '/config.json'
    with open(configFile) as configFile:
        config = json.load(configFile)
            
    serverAddr = ('0.0.0.0', config['server_port'])
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    s.bind(serverAddr)

    while True:
        data,clientAddr = s.recvfrom(1024)
        msg = data.decode('utf-8')
        print('received request: ' + msg)
        processMessage(s, clientAddr, msg)


if __name__ == '__main__':
    main()
