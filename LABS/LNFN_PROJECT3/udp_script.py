from scapy.all import IP, UDP, sr

# Create a UDP packet
udp_packet = IP(dst="192.168.133.1") / UDP(sport=12345, dport=80)

# Send and receive the UDP packet
response = sr(udp_packet, timeout=1, verbose=0)

# Display the response
if response and response[0]:
    response[0].show()
else:
    print("No response received.")
