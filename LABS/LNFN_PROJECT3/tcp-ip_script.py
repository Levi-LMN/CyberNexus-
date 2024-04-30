from scapy.all import IP, TCP, send, sr

def generate_fragmented_packet(src_ip, dst_ip, payload):
    # Create the IP header with a total length of 20 bytes
    ip_header = IP(src=src_ip, dst=dst_ip, len=20)

    # Create the TCP header with the first 8 bytes
    tcp_header = TCP(flags="A", options=[('NOP', None), ('NOP', None)])

    # Combine IP and TCP headers to form the packet
    packet = ip_header / tcp_header / payload

    return packet

# Set your source and new destination IP addresses
src_ip = "192.168.133.132"
new_dst_ip = "192.168.133.1"

# Generate and send the fragmented packet with the new destination IP
payload = b"12345678"  # Example payload
new_fragmented_packet = generate_fragmented_packet(src_ip, new_dst_ip, payload)
new_response = sr(new_fragmented_packet, timeout=1, verbose=0)

# Check if there are any responses
if new_response and new_response[0]:
    # Show the response
    new_response[0].show()
else:
    print("No response received.")
