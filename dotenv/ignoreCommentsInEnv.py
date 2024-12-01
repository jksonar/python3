# Ignore Comments in .env
from dotenv import dotenv_values

config = dotenv_values(".env")
for key, value in config.items():
    print(f"{key}: {value}")
