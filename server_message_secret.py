from scapy.all import sniff, send, IP, UDP

def packet_handler(packet):
    if UDP in packet:
        port = packet[UDP].dport  # Read destination port
        sequence = packet[UDP].sport - 10000  # Extract sequence from source port
        char = chr(port)

        print(f"Received character: {char} (port: {port}, sequence: {sequence})")

        # Send acknowledgment back to client
        ack_packet = IP(dst=packet[IP].src)/UDP(sport=port, dport=packet[UDP].sport)
        send(ack_packet)
        print(f"Sent acknowledgment for sequence {sequence}")

if __name__ == "__main__":
    print("Server is listening for packets...")
    sniff(filter="udp", prn=packet_handler)  # Sniff UDP packets
