from pydantic import BaseModel
from datetime import datetime

class Availability(BaseModel):
    professor_username: str
    start_time: datetime
    end_time: datetime