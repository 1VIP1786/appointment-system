from google.cloud.firestore_v1 import FieldFilter
from google.api_core.exceptions import GoogleAPICallError
from models.appointment import Appointment
from utils.firestore_client import get_firestore_client
import logging
from fastapi import HTTPException

# Initialize Firestore client
db = get_firestore_client()

# Configure logging
logging.basicConfig(level=logging.INFO)

def book_appointment(appointment: Appointment):
    """
    Book a new appointment and add it to Firestore.
    """
    try:
        db.collection("appointments").add(appointment.dict())
        logging.info(f"Appointment booked: {appointment.dict()}")
        return {"message": "Appointment booked successfully"}
    except GoogleAPICallError as e:
        logging.error(f"Failed to book appointment: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

def get_appointments(professor_username: str):
    """
    Retrieve all appointments for a specific professor.
    """
    try:
        appointments = db.collection("appointments").where(
            filter=FieldFilter("professor_username", "==", professor_username)
        ).get()
        logging.info(f"Retrieved appointments for professor '{professor_username}'")
        return [appointment.to_dict() for appointment in appointments]
    except GoogleAPICallError as e:
        logging.error(f"Firestore error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")