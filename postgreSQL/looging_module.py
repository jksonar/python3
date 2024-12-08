import logging
from logging.handlers import RotatingFileHandler

# Configure Logging
LOG_FILE = "app.log"
logging.basicConfig(
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=3),  # Rotate logs
        logging.StreamHandler()  # Log to console
    ]
)

# Example Usage
def log_example():
    logging.info("This is an informational message.")
    logging.warning("This is a warning.")
    logging.error("This is an error.")

log_example()
