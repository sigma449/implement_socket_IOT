import socket
import time

class SenderServer:
    # Let server send something     
    def __init__(self):
        target_ip = "127.0.0.1"     # Server address
        listen_port = 8124          # Server HOST
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)

        #self.client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, True)
        #self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, True)
        
        self.client_socket.connect((target_ip, listen_port))
        self.set_delimiter = True
        #self.client_socket.setblocking(False)

    def socket_send(self, content):
        self.client_socket.send(bytes(str(content), encoding='utf-8'))

if __name__ == '__main__':
    senderServer = SenderServer()
    print("connected to Server")

    while True:
        time.sleep(1)
        detection = {"emotion": 0, "probability":0.64}
        senderServer.socket_send(str(detection))
        print("Sent message: %s" % detection)
        #senderServer.socket_send_all_jetson_packet()
