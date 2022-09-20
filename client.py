import socket 

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
    
# Define the port on which you want to connect to the server
port = 50007
localhost_addr = socket.gethostbyname(socket.gethostname())

# connect to the server on local machine
server_binding = (localhost_addr, port)
cs.connect(server_binding)


#send data to the server
# msg = 'Hi my name is romallamadingdong'
# cs.send(msg.encode('utf-8'))

# Receive data from the server
# data_from_server=cs.recv(100)
# print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))



#open and read the file
with open("in-proj.txt") as f : 
    while True:
        msg=f.readline().rstrip() # can also use format [:-1]
        if msg == '' :   #EOF
            break  
        else:
            cs.send(msg.encode('utf-8'))
            data_from_server=cs.recv(4096)


#     message = f.read.split('/n')
    
# for x in message:
#     cs.send(x.encode('utf-8'))

# close the client socket
cs.close()
exit()