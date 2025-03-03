# Networked Chat Application

This project is a simple networked chat application that demonstrates the use of both TCP and UDP protocols in Python. The application consists of a server and client components, allowing users to send messages and status updates over the network.

## Protocol Specification

The application uses two protocols:

1. **TCP (Transmission Control Protocol)**: 
   - Used for reliable, long-lived connections.
   - Clients connect to the TCP server to send and receive messages.
   - Messages are guaranteed to be delivered in the order they were sent.

2. **UDP (User Datagram Protocol)**: 
   - Used for lightweight, short messages such as status updates.
   - Clients send messages to the UDP server without establishing a connection.
   - Messages may be lost or received out of order, making it suitable for non-critical updates.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd networked-chat-app
   ```

3. Install any required dependencies (if applicable).

## Usage

### Running the Server

To start the TCP server:
```
python server/tcp_server.py
```

To start the UDP server:
```
python server/udp_server.py
```

### Running the Client

To connect to the TCP server:
```
python client/tcp_client.py
```

To send a status update using the UDP client:
```
python client/udp_client.py
```

## Overview

This application serves as a demonstration of socket programming in Python, showcasing how to implement both TCP and UDP communication. The TCP server and client handle reliable message exchanges, while the UDP server and client facilitate quick status updates. This project is ideal for learning about network programming and the differences between connection-oriented and connectionless protocols.