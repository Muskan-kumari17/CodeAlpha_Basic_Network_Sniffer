from scapy.all import sniff, IP, TCP, UDP

def show_packet(packet):
    if IP in packet:
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if TCP in packet:
            print("Protocol: TCP")
            print("Ports:", packet[TCP].sport, "->", packet[TCP].dport)
        elif UDP in packet:
            print("Protocol: UDP")
            print("Ports:", packet[UDP].sport, "->", packet[UDP].dport)
        else:
            print("Protocol:", packet[IP].proto)

        print("-" * 30)

print("Basic Network Sniffer Started...")
sniff(filter="ip", prn=show_packet, count=10, store=False)
print("Capture complete.")
