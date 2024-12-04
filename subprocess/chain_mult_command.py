# Chain Multiple Commands
import subprocess

p1 = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", ".py"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits
output = p2.communicate()[0]
print(output)
