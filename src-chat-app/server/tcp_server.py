import socket
import threading
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TCPServer:
    def __init__(self, host='127.0.0.1', port=65432):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server_socket.bind((host, port))
            self.server_socket.listen()
            logging.info(f'TCP Server listening on {host}:{port}')
        except socket.error as e:
            logging.error(f"Failed to bind TCP server socket: {e}")
            raise

        self.clients = []
        self.client_names = {}
        self.lock = threading.Lock()

    def broadcast(self, message, sender_socket):
        with self.lock:
            for client_socket in self.clients:
                if client_socket != sender_socket:
                    try:
                        client_socket.sendall(message.encode('utf-8'))
                        logging.info(f"Broadcasted message: {message}")
                    except BrokenPipeError:
                        self.clients.remove(client_socket)
                        del self.client_names[client_socket]
                        logging.warning(f"Removed client due to BrokenPipeError: {client_socket}")
                    except socket.error as e:
                        logging.error(f"Socket error while broadcasting: {e}")

    def handle_client(self, client_socket, address):
        logging.info(f'Connection from {address} has been established!')
        with self.lock:
            self.clients.append(client_socket)
        try:
            while True:
                try:
                    message = client_socket.recv(1024).decode('utf-8')
                    if not message:
                        break
                    if message.startswith("NAME:"):
                        display_name = message.split(":", 1)[1]
                        with self.lock:
                            self.client_names[client_socket] = display_name
                        logging.info(f'{address} set their display name to {display_name}')
                    else:
                        display_name = self.client_names.get(client_socket, str(address))
                        logging.info(f'Received from {display_name}: {message}')
                        self.broadcast(f'{display_name}: {message}', client_socket)
                except socket.timeout:
                    logging.warning(f"Connection timed out for {address}")
                    break
                except socket.error as e:
                    logging.error(f"Socket error for {address}: {e}")
                    break
        except ConnectionResetError:
            logging.warning(f"Connection reset by {address}")
        finally:
            with self.lock:
                self.clients.remove(client_socket)
                if client_socket in self.client_names:
                    del self.client_names[client_socket]
            client_socket.close()
            logging.info(f'Connection from {address} has been closed.')

    def get_user_list(self):
        with self.lock:
            user_list = list(self.client_names.values())
            logging.info(f"Current user list: {user_list}")
            return user_list

    def start(self):
        while True:
            try:
                client_socket, address = self.server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
                client_thread.start()
                logging.info(f"Started thread for {address}")
            except socket.error as e:
                logging.error(f"Socket error while accepting connection: {e}")

if __name__ == '__main__':
    try:
        tcp_server = TCPServer()
        tcp_server.start()
    except Exception as e:
        logging.error(f"Failed to start TCP server: {e}")