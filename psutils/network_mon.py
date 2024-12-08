import psutil

# Get Network Statistics
network_stats = psutil.net_io_counters()
print(f"Bytes Sent: {network_stats.bytes_sent // 1024} KB")
print(f"Bytes Received: {network_stats.bytes_recv // 1024} KB")

# Get Network Interface Information
network_info = psutil.net_if_addrs()
for interface, addresses in network_info.items():
    print(f"Interface: {interface}")
    for addr in addresses:
        print(f"  Address: {addr.address}, Netmask: {addr.netmask}, Broadcast: {addr.broadcast}")
