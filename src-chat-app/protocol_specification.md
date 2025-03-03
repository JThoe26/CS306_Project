# Protocol Specification for Networked Chat Application

## Overview
This document outlines the protocol specifications for the CS306_Project chat application, which utilizes both TCP and UDP protocols for communication. The application consists of a TCP server and a UDP server, each serving different purposes in the chat functionality.

## Protocols Used
1. **TCP (Transmission Control Protocol)**
   - Used for reliable, ordered, and error-checked delivery of messages.
   - Suitable for long-lived connections where message integrity is crucial.

2. **UDP (User Datagram Protocol)**
   - Used for sending short messages without establishing a connection.
   - Suitable for lightweight, quick status updates where speed is more critical than reliability.

## Message Formats

### TCP Message Format
- **Structure**: 
  ```
  <username>:<message>
  ```
- **Example**: 
  ```
  Jack:Hello, how are you?
  ```
- **Behavior**:
  - The client connects to the TCP server and sends messages in the above format.
  - The server acknowledges receipt of the message and can send back responses.
  - Each message is processed in the order received.

### UDP Message Format
- **Structure**: 
  ```
  <username>:<status_update>
  ```
- **Example**: 
  ```
  Bob:Online
  ```
- **Behavior**:
  - The client sends status updates to the UDP server using the above format.
  - The server does not guarantee message delivery or order.
  - Responses from the server are optional and may not be sent.

## Connection Management

### TCP Server
- Listens on a specified port for incoming TCP connections.
- Accepts multiple client connections using threading to handle each client in a separate thread.
- Maintains the state of each connection and ensures reliable message delivery.

### UDP Server
- Listens on a specified port for incoming UDP messages.
- Does not maintain connection state; each message is handled independently.
- Suitable for handling bursts of short messages efficiently.

## Client Behavior

### TCP Client
- Connects to the TCP server and sends messages formatted as specified.
- Waits for responses from the server and displays them to the user.
- Handles user input in a loop, allowing for continuous message exchange.

### UDP Client
- Sends short status update messages to the UDP server.
- Listens for optional responses from the server.
- Designed for quick interactions without the overhead of maintaining a connection.

## Conclusion
This protocol specification serves as a guide for implementing the networked chat application, ensuring that both TCP and UDP communications are handled appropriately according to their respective characteristics and intended use cases.