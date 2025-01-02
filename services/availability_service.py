from google.cloud.firestore_v1 import FieldFilter
from google.api_core.exceptions import GoogleAPICallError
from utils.firestore_client import get_firestore_client
import logging
from fastapi import HTTPException

# Initialize Firestore client
db = get_firestore_client()

# Configure logging
logging.basicConfig(level=logging.INFO)

def add_availability(availability):
    """
    Add a new availability slot to Firestore.
    """
    try:
        db.collection("availabilities").add(availability.dict())
        logging.info(f"Availability added: {availability.dict()}")
        return {"message": "Availability added successfully"}
    except GoogleAPICallError as e:
        logging.error(f"Failed to add availability: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

def get_availabilities(professor_username: str):
    """
    Retrieve all availability slots for a specific professor.
    """
    try:
        availabilities = db.collection("availabilities").where(
            filter=FieldFilter("professor_username", "==", professor_username)
        ).get()
        logging.info(f"Retrieved availabilities for professor '{professor_username}'")
        return [availability.to_dict() for availability in availabilities]
    except GoogleAPICallError as e:
        logging.error(f"Firestore error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")