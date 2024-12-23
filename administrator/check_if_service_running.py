import os

def check_service(service_name):
    status = os.system(f"systemctl is-active --quiet {service_name}")
    if status == 0:
        print(f"{service_name} is running.")
    else:
        print(f"{service_name} is not running.")

check_service("ssh")
