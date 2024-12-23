import psutil

def list_processes():
    for process in psutil.process_iter(['pid', 'name', 'username']):
        print(process.info)

list_processes()
