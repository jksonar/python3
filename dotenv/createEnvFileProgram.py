# Create a .env File Programmatically
with open(".env", "w") as file:
    file.write("NEW_VAR=42\n")
    file.write("DEBUG=true\n")
print(".env file created")
