from scapy.all import IP, ICMP, sr

# Create an ICMP (ping) packet
icmp_packet = IP(dst="192.168.133.1") / ICMP()

# Send and receive the ICMP packet
response = sr(icmp_packet, timeout=1, verbose=0)

# Display the response
if response and response[0]:
    response[0].show()
else:
    print("No response received.")

