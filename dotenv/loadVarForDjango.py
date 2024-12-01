# Load Variables for Flask/Django Configurations
from dotenv import load_dotenv
import os

load_dotenv()

# Example usage in Flask
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
