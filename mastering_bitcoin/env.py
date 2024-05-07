from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class ENV():
    def __init__(self):
        self.service_url = os.getenv("SERVICE_URL")
