import socket
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_tcp_client(server_ip, server_port, display_name):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
            tcp_socket.connect((server_ip, server_port))
            logging.info("Connected to TCP server.")
            
            # Send display name to the server
            tcp_socket.sendall(f"NAME:{display_name}".encode())
            logging.info(f"Sent display name: {display_name}")

            while True:
                message = input("Enter message to send (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    logging.info("Exiting TCP client.")
                    break
                tcp_socket.sendall(f"{message}".encode())
                logging.info(f"Sent message: {message}")
                response = tcp_socket.recv(1024)
                logging.info(f"Received from server: {response.decode()}")
    except ConnectionRefusedError:
        logging.error("Connection refused by the server.")
    except ConnectionResetError:
        logging.error("Connection reset by the server.")
    except socket.timeout:
        logging.error("Connection timed out.")
    except socket.error as e:
        logging.error(f"Socket error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

def start_udp_client(server_ip, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
            logging.info("UDP client ready.")
            
            # Request list of users from the server
            udp_socket.sendto("GET_USERS".encode(), (server_ip, server_port))
            logging.info("Requested list of users from UDP server.")
            response, _ = udp_socket.recvfrom(1024)
            logging.info(f"Received list of users: {response.decode()}")
    except socket.timeout:
        logging.error("Connection timed out.")
    except socket.error as e:
        logging.error(f"Socket error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    SERVER_IP = '127.0.0.1'
    TCP_SERVER_PORT = 65432 
    UDP_SERVER_PORT = 65433 

    try:
        display_name = input("Enter your display name: ").strip()
        logging.info(f"Display name entered: {display_name}")
        protocol = input("Choose function (CHAT/USERS): ").strip().upper()
        logging.info(f"Protocol chosen: {protocol}")
        if protocol == 'CHAT':
            start_tcp_client(SERVER_IP, TCP_SERVER_PORT, display_name)
        elif protocol == 'USERS':
            start_udp_client(SERVER_IP, UDP_SERVER_PORT)
        else:
            logging.error("Invalid protocol. Please choose either 'CHAT' or 'USERS'.")
            print("Invalid protocol. Please choose either 'CHAT' or 'USERS'.")
    except Exception as e:
        logging.error(f"Unexpected error in main block: {e}")