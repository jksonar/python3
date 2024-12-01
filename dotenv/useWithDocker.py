# Use with Docker
# Inside .env
# IMAGE_NAME=my-docker-image
# TAG=latest

from dotenv import load_dotenv
import os

load_dotenv()

docker_command = f"docker build -t {os.getenv('IMAGE_NAME')}:{os.getenv('TAG')} ."
print(docker_command)
