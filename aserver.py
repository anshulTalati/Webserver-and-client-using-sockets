#1001570332_Talati_Anshul


import socket
import sys
from threading import Thread
from SocketServer import ThreadingMixIn


TCP_IP = 'localhost'
TCP_PORT = int(sys.argv[1])
BUFFER_SIZE = 1024

class ClientThread(Thread):
      
    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print " New thread started for "+ip+":"+str(port)
     
     # Function to extract the requested file name from the request data
    def extract_filename(self, raw_data):
        try:
            data_list = raw_data.split('\\r\\n')
            return data_list[0].split(' ')[1].lstrip('/')
        except Exception as e:
            pass
        return ''
     
    def run(self):
        # Printing out server params
        print 'HostName: ', self.ip
        print 'Socket Family: ', self.sock.family
        print 'Socket Type', self.sock.type
        print 'Socket Protocol', self.sock.proto
        print 'Peer Name', self.sock.getpeername()

        # Data received from the client
        data = self.sock.recv(1024)
        raw_data =  repr(data)

        # Filename extracted from req data
        filename = self.extract_filename(raw_data.strip("'"))
        
        # Incase no file name is present then server status is reported
        if not filename:
            self.sock.send('HTTP/1.1 200 OK Request\nContent-Type: text/html\n\n<body>Server is Running</body>')
        elif filename in ["anshul1.txt", "anshul2.txt"]:
            # If file found then it is read, buffered
            f = open(filename,'rb')
            buffered_data = ''
            while True:
                l = f.read(BUFFER_SIZE)
                while (l):
                    buffered_data = buffered_data + l
                    l = f.read(BUFFER_SIZE)
                if not l:
                    f.close()
                    break
            
            # Positive response with file data is sent to client
            self.sock.send(
                'HTTP/1.0 200 OK'+
                '\nHost: '+TCP_IP+
                '\nContent-Type: text/plain; charset=utf-8'+
                '\nContent-Disposition: attachment; filename="received.txt"'+
                '\nContent-Length: '+str(len(buffered_data))+
                '\n\n'+
                buffered_data)

        else:
            # If invalid file name given file not found
            self.sock.send('HTTP/1.1 400 Bad Request\nContent-Type: text/html\n\n<body>Not Found</body>')
        self.sock.close()


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    # Multi Threaded Server started
    tcpsock.listen(5)
    print "Waiting for incoming connections..."
    (conn, (ip,port)) = tcpsock.accept()
    print 'Got connection from ', (ip,port)
    # New thread started
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()