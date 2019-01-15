#1001570332_Talati_Anshul

import sys
import socket
import time

TCP_IP = sys.argv[1] #'localhost'
TCP_PORT = int(sys.argv[2]) #9001
BUFFER_SIZE = 1024

try:
    requested_filename = sys.argv[3]
except:
    requested_filename = ''
# Server GET Request constructed
get_request = 'GET /{req_filename} HTTP/1.1'.format(req_filename=requested_filename)
print get_request

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t = time.time()

# Server connection established with client
s.connect((TCP_IP, TCP_PORT))
print 'RTT Connection: ', time.time()-t
t = time.time()

# Client reqest sent to server to get file
s.send(get_request)

# Received file buffered and loaded into variable
buffered_data = ''
while True:
    data = s.recv(BUFFER_SIZE)
    if data:
        buffered_data = buffered_data + data
    else:
        break

print 'HostName: ', TCP_IP
print 'Socket Family: ', s.family
print 'Socket Type: ', s.type
print 'Peer Name: ', s.getpeername()
    
s.close()
print 'Connection closed'
print 'RTT Get File: ', time.time()-t

# Process buffered data
if buffered_data and buffered_data.startswith('HTTP/1.1 400'):
    print 'File not found!'
else:
    # Buffered data split into header and downloadable file data.
    header_data, file_data = buffered_data.split('\n\n', 1)
    with open('received_file', 'wb') as f:
        # write data to a file
        f.write(file_data)
        f.close()
        print('File saved successfully.')
