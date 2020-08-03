import socket
import sys

class Send:
    def __init__(self,hostIp,port):
        try:
            self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((hostIp,port))
            self.s.listen(5)#Five connection before the port starts rejecting the same
        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()
	
            
    def sendFile(self,filePath):
        conn, addr = self.s.accept() 
        print ('Connection established to', addr) 
        f = open(filePath,'rb')  
        data = f.read()  
        conn.send(data)  
        f.close()
        print("Data sent successfully")
        conn.close()
