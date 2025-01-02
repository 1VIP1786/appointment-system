Appointment Booking System
==========================

A FastAPI web application designed for efficient appointment scheduling between students and professors.

Key Features
-------------
- User Authentication: Secure sign-up and login for students and professors.
- Availability Management: Professors set available time slots.
- Appointment Booking: Students book appointments based on available slots.
- Appointment Tracking: Professors can track their scheduled appointments.

Technologies
-------------
- Backend: FastAPI
- Database: Google Cloud Firestore
- Deployment: Google Cloud Platform (Compute Engine)
- Authentication: Bcrypt for password hashing
- Testing: Postman, cURL

Getting Started
---------------
### Requirements
- Python 3.8+
- Google Cloud account with Firestore access
- Firestore credentials JSON file

### Local Setup

1. Clone the Repo:
    ```bash
    git clone https://github.com/1VIP1786/appointment-system.git
    cd appointment-system
    ```

2. Set Up Virtual Environment & Install Dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Configure Environment Variables:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
    ```

4. Run the Application:
    ```bash
    uvicorn app:app --reload
    ```

5. Access the App: Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

API Endpoints
-------------
### Authentication

- Sign Up (POST /signup):
    ```json
    {
        "username": "newuser",
        "password": "newpass",
        "role": "student"
    }
    ```

- Log In (POST /login):
    ```json
    {
        "username": "newuser",
        "password": "newpass"
    }
    ```

### Availability

- Add Availability (POST /professor/availability):
    ```json
    {
        "professor_username": "prof1",
        "start_time": "2023-10-10T09:00:00",
        "end_time": "2023-10-10T10:00:00"
    }
    ```

- View Available Slots (GET /student/availabilities/{professor_username})

### Appointments

- Book Appointment (POST /student/book-appointment):
    ```json
    {
        "student_username": "student1",
        "professor_username": "prof1",
        "start_time": "2023-10-10T09:00:00",
        "end_time": "2023-10-10T10:00:00"
    }
    ```

- View Appointments (GET /professor/appointments/{professor_username})

Deployment to Google Cloud
---------------------------
### Steps:

1. Create and Set Up VM: In the [GCP Console](https://console.cloud.google.com/), create a new VM instance in Compute Engine.

2. SSH Into Instance & Install Dependencies:
    ```bash
    gcloud compute ssh --zone=your-instance-zone your-instance-name
    sudo apt update
    sudo apt install python3 python3-pip -y
    pip install -r requirements.txt
    ```

3. Run the Application:
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```

4. Set Firewall Rules: Configure inbound traffic on port 8000.

Contributing
------------
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/YourFeatureName
    ```
3. Commit changes:
    ```bash
    git commit -m 'Add new feature'
    ```
4. Push the branch:
    ```bash
    git push origin feature/YourFeatureName
    ```
5. Open a pull request.

License
-------
This project is licensed under the **MIT License**.

Contact
-------
For questions or feedback, feel free to reach out:

- **Vipul Patil**
- Email: [vipulpatil@gmail.com](mailto:vipulpatil1786@gmail.com)
- GitHub: [1VIP178](https://github.com/1VIP1786)

