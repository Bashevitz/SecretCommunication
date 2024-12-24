from scapy.all import send, IP, UDP

def send_message(server_ip, message):
    for i, char in enumerate(message):
        port = ord(char)  # Convert character to ASCII
        packet = IP(dst=server_ip)/UDP(dport=port, sport=10000+i)  # Sequence in source port
        send(packet)
        print(f"Sent packet to port {port} ({char}), sequence {i}")

if __name__ == "__main__":
    server_ip = "192.168.1.2"  # Replace with your server's IP address
    message = input("Enter the message to send: ")
    send_message(server_ip, message)
