import subprocess

def system_update():
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])
    print("System updated and upgraded.")

system_update()
