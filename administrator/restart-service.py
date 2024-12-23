# Restart Service
import subprocess

def restart_service(service_name):
    subprocess.run(["sudo", "systemctl", "restart", service_name])
    print(f"{service_name} restarted.")

restart_service("apache2")
