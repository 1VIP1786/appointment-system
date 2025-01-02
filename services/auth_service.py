import bcrypt
from google.cloud import firestore
from google.cloud.firestore_v1 import FieldFilter  # Import FieldFilter
from google.api_core.exceptions import GoogleAPICallError
import os
from dotenv import load_dotenv
import logging
from fastapi import HTTPException

# Load environment variables
load_dotenv()

# Initialize Firestore client
db = firestore.Client.from_service_account_json(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

# Configure logging
logging.basicConfig(level=logging.INFO)

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hashed version.
    """
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def authenticate_user(username: str, password: str):
    """
    Authenticate a user by checking if the username and password match a record in Firestore.
    """
    try:
        # Use FieldFilter for Firestore query
        user_ref = db.collection("users").where(filter=FieldFilter("username", "==", username)).get()
        if user_ref:
            user_data = user_ref[0].to_dict()
            if verify_password(password, user_data["password"]):  # Verify hashed password
                logging.info(f"User authenticated: {username}")
                return user_data
        logging.warning(f"Authentication failed: Invalid credentials for user '{username}'")
        return None
    except GoogleAPICallError as e:
        logging.error(f"Firestore error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

def create_user(username: str, password: str, role: str):
    """
    Create a new user in Firestore.
    """
    try:
        # Check if the username already exists
        user_ref = db.collection("users").where(filter=FieldFilter("username", "==", username)).get()
        if user_ref:
            logging.warning(f"Signup failed: Username '{username}' already exists")
            raise HTTPException(status_code=400, detail="Username already exists")
        
        # Hash the password
        hashed_password = hash_password(password)
        
        # Create the user
        user_data = {
            "username": username,
            "password": hashed_password,  # Store hashed password
            "role": role
        }
        db.collection("users").add(user_data)
        logging.info(f"User created: {username}")
        return {"message": "Signup successful"}
    except GoogleAPICallError as e:
        logging.error(f"Firestore error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    except HTTPException as e:
        # Re-raise HTTPException for duplicate usernames
        raise e
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")