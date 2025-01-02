from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.user import User
from models.availability import Availability
from models.appointment import Appointment
from services.auth_service import authenticate_user, create_user
from services.availability_service import add_availability, get_availabilities
from services.appointment_service import book_appointment, get_appointments

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

class LoginRequest(BaseModel):
    username: str
    password: str

class SignupRequest(BaseModel):
    username: str
    password: str
    role: str  # "student" or "professor"

@app.post("/login")
def login(request: LoginRequest):
    user = authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user": user}

@app.post("/signup")
def signup(request: SignupRequest):
    """
    Signup a new user.
    """
    # Check if the username already exists
    if authenticate_user(request.username, request.password):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Create the user
    create_user(request.username, request.password, request.role)
    return {"message": "Signup successful"}

# Professor adds availability
@app.post("/professor/availability")
def add_professor_availability(availability: Availability):
    add_availability(availability)
    return {"message": "Availability added successfully"}

# Student views availabilities
@app.get("/student/availabilities/{professor_username}")
def view_availabilities(professor_username: str):
    availabilities = get_availabilities(professor_username)
    return {"availabilities": availabilities}

# Student books appointment
@app.post("/student/book-appointment")
def book_student_appointment(appointment: Appointment):
    book_appointment(appointment)
    return {"message": "Appointment booked successfully"}

# Professor views appointments
@app.get("/professor/appointments/{professor_username}")
def view_appointments(professor_username: str):
    appointments = get_appointments(professor_username)
    return {"appointments": appointments}