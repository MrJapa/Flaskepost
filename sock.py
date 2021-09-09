# first of all import the socket library
import socket            
 
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 31337               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs
while True:
    c, addr = s.accept()    
    print ('Got connection from', addr )

    int.from_bytes(c.recv(1024),byteorder="little")
    tal = int.from_bytes(c.recv(1024),byteorder="little")
    print(tal)

    tal += 1
    print(tal)
    
    # Close the connection with the client
    c.close()
    
    
    # Breaking once connection closed
    break


HOST2 = '172.17.10.3'
PORT2 = 31337
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.connect((HOST2, PORT2))
    x.sendall(int.to_bytes(tal),byteorder="little")
    data = x.recv(1024)
    print('Received', repr(data))
    c.close()
    