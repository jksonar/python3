# Read All Variables into a Dictionary
from dotenv import dotenv_values

config = dotenv_values(".env")
print(config)
