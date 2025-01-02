Appointment Booking System : 
The Appointment Booking System is a web application built with FastAPI, designed to facilitate seamless appointment scheduling between students and professors. It includes features for user authentication, managing availability, and booking appointments.

Key Features
User Authentication:

Students and professors can create accounts and log in securely.

Availability Management:

Professors can define their available time slots.

Appointment Booking:

Students can view available slots and book appointments.

Appointment Tracking:

Professors can view their scheduled appointments.

Technologies
Backend Framework: FastAPI

Database: Google Cloud Firestore

Deployment Platform: Google Cloud Platform (GCP) Compute Engine

Authentication: Bcrypt for secure password hashing

Testing Tools: Postman, cURL

##Getting Started
###Prerequisites
Python 3.8 or higher: Ensure Python is installed on your system.

Google Cloud Account: Create a Google Cloud account and enable Firestore.

Firestore Credentials: Download the Firestore credentials JSON file.

Local Setup
###Clone the Repository:

bash
Copy
git clone https://github.com/1VIP1786/appointment-system.git
cd appointment-system
Set Up a Virtual Environment:

bash
Copy
python3 -m virtualenv venv
source venv/bin/activate
Install Required Packages:

bash
Copy
pip install -r requirements.txt
Configure Environment Variables:

###Set the path to your Firestore credentials:

bash
Copy
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
Run the Application:

bash
Copy
uvicorn app:app --reload
Access the Application:

Open your browser and navigate to:

Copy
http://127.0.0.1:8000
API Documentation
Authentication
Signup:

POST /signup

Request Body:

json
Copy
{
  "username": "newuser",
  "password": "newpass",
  "role": "student"
}
Login:

POST /login

Request Body:

json
Copy
{
  "username": "newuser",
  "password": "newpass"
}
Availability
Add Availability:

POST /professor/availability

Request Body:

json
Copy
{
  "professor_username": "prof1",
  "start_time": "2023-10-10T09:00:00",
  "end_time": "2023-10-10T10:00:00"
}
View Availabilities:

GET /student/availabilities/{professor_username}

Appointments
Book Appointment:

POST /student/book-appointment

Request Body:

json
Copy
{
  "student_username": "student1",
  "professor_username": "prof1",
  "start_time": "2023-10-10T09:00:00",
  "end_time": "2023-10-10T10:00:00"
}
View Appointments:

GET /professor/appointments/{professor_username}

Deployment to GCP
Steps
Create a Compute Engine Instance:

Log in to the GCP Console.

Navigate to Compute Engine → VM Instances.

Create a new instance with a suitable machine type (e.g., e2-micro).

Deploy the Application:

SSH into the instance:

bash
Copy
gcloud compute ssh --zone=your-instance-zone your-instance-name
Install dependencies:

bash
Copy
sudo apt update
sudo apt install python3 python3-pip -y
pip install -r requirements.txt
Run the application:

bash
Copy
uvicorn app:app --host 0.0.0.0 --port 8000
Configure Firewall Rules:

Allow inbound traffic on port 8000 for the instance.

Contributing
We welcome contributions! Here’s how you can help:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

License
This project is licensed under the MIT License. For more details, see the LICENSE file.

Contact
For questions or feedback, feel free to reach out:

Vipul
Email: vipul@example.com
GitHub: 1VIP178
