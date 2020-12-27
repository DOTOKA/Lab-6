import socket 
import math 
import errno 
import sys
from multiprocessing import Process

ThreadCount = 0
if __name__ == '__main__':
   
     S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     host = ''
     port = 5000

     try:
        S.bind((host,port))
     except socket.error as e:
        print (str(e))
        sys.exit()
 
     S.listen(5)
    
     def Mula(server):

        while True:
            ch = server.recv(1024).decode()

            #Calculating Log
            if ch == '1':
                numb = server.recv(1024).decode()
                calc = math.log(float(numb))

            #Calculating Square Root
            elif ch  == '2':
                numb = server.recv(1024).decode()
                calc = math.sqrt(float(numb))

            #Calculating Exponential
            elif ch  == '3':
                numb = server.recv(1024).decode()
                calc = math.exp(float(numb))

            elif ch == '9':
                server.close()
                break

            server.sendall(str(calc).encode())


     while True:
        try:
            server, addr = S.accept()
            print ('\n Sucessfully Connected !! ')
            print('Connected to: ' + addr[0] + ':' + str(addr[1]))
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount))        
            p = Process(target = Mula, args=(server,))
            p.start()

        except socket.error:
            print ('an exception occurred!')

     S.close()

