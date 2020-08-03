import socket
import sys

class Recive:
    def __init__(self,hostIp,port):
        self.hostIp=hostIp
        self.port=port
    
    def recive(self,dstPath):
        try:
            self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.hostIp, self.port))#Five connection before the port starts rejecting the same
        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()
        file = open(dstPath,"wb")
        while True:
            print('Reciving data...')
            data = self.s.recv(1024)
            if not data:
                break
            file.write(data)
        file.close()
        print('File recived successfully')
        self.s.close()