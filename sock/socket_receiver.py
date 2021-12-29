import socket
import time

class ReceiverServer:
    def __init__(self):
        host_ip = "127.0.0.1"   # Receiver server IP
        listen_port = 8124      # Receiver server HOST

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host_ip, listen_port))  # ADD IP HERE
        self.server_socket.listen(5)

        print('server start at: %s:%s' % (host_ip, listen_port))
        print('wait for connection...') 


    def socket_accept(self):
        self.connection, addr = self.server_socket.accept()
        addr = str(addr)
        print('connected by client address: %s' % (addr))

        return addr

    def socket_send(self, content):
        self.connection.write(bytes(content, encoding='utf-8'))
        
    def socket_read(self):
        content = self.connection.recv(1024)
        #if content != None and content !=b'':
            #print("receive time from client: " + str(content))
        return content

if __name__ == '__main__':
    receiverServer = ReceiverServer()

    receive_ip = receiverServer.socket_accept()
    print(f"get connect: {receive_ip}")
    while True:
        reData = receiverServer.socket_read()
        if reData != None and reData !=b'':
            print('    Receiver Data:%s' % reData) 

        #time.sleep(0.1) # receiver interval 
