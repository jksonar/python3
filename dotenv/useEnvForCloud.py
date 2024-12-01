# Use .env for Cloud Configurations
from dotenv import load_dotenv
import os

load_dotenv()

cloud_storage = os.getenv("CLOUD_STORAGE_URL")
print(cloud_storage)
