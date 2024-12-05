# Environment Variables
import subprocess

env = {"MY_VAR": "Hello, Environment!"}
result = subprocess.run(["printenv", "MY_VAR"], capture_output=True, text=True, env=env)
print(result.stdout)  # Output: Hello, Environment!
