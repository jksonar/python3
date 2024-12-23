# Manage Firewall (UFW)
import subprocess

def enable_ufw():
    subprocess.run(["sudo", "ufw", "enable"])
    print("Firewall enabled.")

def add_firewall_rule(port):
    subprocess.run(["sudo", "ufw", "allow", f"{port}"])
    print(f"Port {port} opened.")

enable_ufw()
add_firewall_rule(22)  # Open SSH port
