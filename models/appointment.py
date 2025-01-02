from pydantic import BaseModel
from datetime import datetime

class Appointment(BaseModel):
    student_username: str
    professor_username: str
    start_time: datetime
    end_time: datetime