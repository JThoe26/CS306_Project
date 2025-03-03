import socket
import threading
import logging
from tcp_server import TCPServer

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UDPServer:
    def __init__(self, tcp_server, host='127.0.0.1', port=65433):
        self.tcp_server = tcp_server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.server_socket.bind((host, port))
            logging.info(f'UDP Server listening on {host}:{port}')
        except socket.error as e:
            logging.error(f"Failed to bind UDP server socket: {e}")
            raise

    def handle_request(self, data, address):
        try:
            message = data.decode('utf-8')
            logging.info(f"Received request from {address}: {message}")
            if message == 'GET_USERS':
                user_list = self.tcp_server.get_user_list()
                response = ', '.join(user_list)
                self.server_socket.sendto(response.encode('utf-8'), address)
                logging.info(f"Sent user list to {address}: {response}")
            else:
                logging.warning(f"Unknown request from {address}: {message}")
        except Exception as e:
            logging.error(f"Error handling request from {address}: {e}")

    def start(self):
        while True:
            try:
                data, address = self.server_socket.recvfrom(1024)
                logging.info(f"Received data from {address}")
                request_thread = threading.Thread(target=self.handle_request, args=(data, address))
                request_thread.start()
                logging.info(f"Started thread to handle request from {address}")
            except socket.error as e:
                logging.error(f"Socket error: {e}")
            except Exception as e:
                logging.error(f"Unexpected error: {e}")

if __name__ == '__main__':
    try:
        tcp_server = TCPServer()
        threading.Thread(target=tcp_server.start).start()
        udp_server = UDPServer(tcp_server)
        udp_server.start()
    except Exception as e:
        logging.error(f"Failed to start servers: {e}")