from google.cloud import firestore
import os
from dotenv import load_dotenv

load_dotenv()

def get_firestore_client():
    """
    Initialize and return a Firestore client.
    """
    return firestore.Client.from_service_account_json(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))