import logging
import os

# Create logs directory automatically
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/encryption.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_message(message):
    logging.info(message)