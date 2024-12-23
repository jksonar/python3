import psutil

def network_stats():
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent}")
    print(f"Bytes Received: {net_io.bytes_recv}")

network_stats()
