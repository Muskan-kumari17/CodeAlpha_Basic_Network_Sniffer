from scapy.all import sniff, IP, TCP, UDP, ICMP


packet_count = 0


def packet_callback(packet):
    global packet_count

    if IP in packet:
        packet_count += 1

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        source_port = "N/A"
        destination_port = "N/A"

        if TCP in packet:
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        elif ICMP in packet:
            protocol = "ICMP"

        else:
            protocol = "Other"

        print("\n===================================")
        print("Packet Number   :", packet_count)
        print("Source IP       :", source_ip)
        print("Destination IP  :", destination_ip)
        print("Protocol        :", protocol)
        print("Source Port     :", source_port)
        print("Destination Port:", destination_port)

        if packet.haslayer("Raw"):
            payload = packet["Raw"].load
            print("Payload         :", payload[:50])
        else:
            print("Payload         : No Raw Payload")


print("===================================")
print("     CODEALPHA NETWORK SNIFFER")
print("===================================")
print("Starting packet capture...")
print("Press Ctrl+C to stop.\n")

sniff(prn=packet_callback, store=False)