### README.md

# Secure Message Transmission Using Scapy

This project demonstrates secure communication between a client and a server using UDP packets. Each character of the message is transmitted as an empty UDP packet to a port corresponding to the character's ASCII value.

---

## Prerequisites

1. **Python 3.8+**: Ensure Python is installed on both machines.
2. **Scapy**: Install Scapy by running:
   ```bash
   pip install scapy
   ```
3. **Two Machines**:
   - One for running the server script.
   - Another for running the client script.
4. **Network Configuration**:
   - Both machines must be on the same network.
   - Ensure the server's IP address is reachable from the client.

---

## Files

- `py.client_message_secret.py`: The client script that sends the message.
- `py.server_message_secret.py`: The server script that receives and decodes the message.

---

## Running the Scripts

### 1. On the Server (Machine A)

1. Open a terminal.
2. Run the server script:
   ```bash
   python3 py.server_message_secret.py
   ```
3. The server will start listening for UDP packets and display received characters.

### 2. On the Client (Machine B)

1. Open a terminal.
2. Run the client script:
   ```bash
   python3 py.client_message_secret.py
   ```
3. Enter the message you want to send when prompted:
   ```plaintext
   Enter the message to send: Hello
   ```

4. The client will send the message character by character as UDP packets to the server.

---

## Example Output

### Server Output
```plaintext
Server is listening for packets...
Received character: H (port: 72, sequence: 0)
Received character: e (port: 101, sequence: 1)
Received character: l (port: 108, sequence: 2)
Received character: l (port: 108, sequence: 3)
Received character: o (port: 111, sequence: 4)
```

### Client Output
```plaintext
Enter the message to send: Hello
Sent packet to port 72 (H), sequence 0
Sent packet to port 101 (e), sequence 1
Sent packet to port 108 (l), sequence 2
Sent packet to port 108 (l), sequence 3
Sent packet to port 111 (o), sequence 4
```

---
