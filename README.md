Appointment Scheduling System
A FastAPI-based web application for seamless appointment scheduling between students and professors. It offers user authentication, availability management, and appointment tracking.

Key Features
User Authentication: Secure account creation and login for both students and professors.
Availability Management: Professors can set available time slots.
Appointment Booking: Students can book appointments based on available slots.
Appointment Tracking: Professors can view their upcoming appointments.
Tech Stack
Backend: FastAPI
Database: Google Cloud Firestore
Deployment: Google Cloud Platform (Compute Engine)
Authentication: Bcrypt for password hashing
Testing: Postman, cURL
Getting Started
Requirements
Python 3.8+
Google Cloud account with Firestore
Firestore credentials JSON file
Local Setup
Clone the Repo:

bash
Copy code
git clone https://github.com/1VIP1786/appointment-system.git
cd appointment-system
Set Up Virtual Environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Configure Environment Variables:

bash
Copy code
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
Run the App:

bash
Copy code
uvicorn app:app --reload
Access the App:
Open http://127.0.0.1:8000

API Endpoints
Authentication
Sign Up (POST /signup):
{"username": "newuser", "password": "newpass", "role": "student"}

Log In (POST /login):
{"username": "newuser", "password": "newpass"}

Availability
Add Availability (POST /professor/availability):
{"professor_username": "prof1", "start_time": "2023-10-10T09:00:00", "end_time": "2023-10-10T10:00:00"}

View Available Slots (GET /student/availabilities/{professor_username})

Appointments
Book Appointment (POST /student/book-appointment):
{"student_username": "student1", "professor_username": "prof1", "start_time": "2023-10-10T09:00:00", "end_time": "2023-10-10T10:00:00"}

View Appointments (GET /professor/appointments/{professor_username})

Deployment to Google Cloud
Create a VM Instance:
In GCP Console, go to Compute Engine → VM Instances and create a new VM instance.

SSH into the Instance:

bash
Copy code
gcloud compute ssh --zone=your-instance-zone your-instance-name
Install Dependencies:

bash
Copy code
sudo apt update
sudo apt install python3 python3-pip -y
pip install -r requirements.txt
Run the App:

bash
Copy code
uvicorn app:app --host 0.0.0.0 --port 8000
Set Firewall Rules:
Open port 8000 for external traffic.

Contributing
Fork the repository.
Create a feature branch:
git checkout -b feature/YourFeatureName
Commit your changes:
git commit -m 'Add new feature'
Push to your fork:
git push origin feature/YourFeatureName
Open a pull request.
License
This project is licensed under the MIT License.

Contact
For questions or feedback:

Vipul patil
Email: vipulpatil1786@gmail.com
GitHub: 1VIP1786
PORTFOLIO : VIPULPATIL.LIVE
