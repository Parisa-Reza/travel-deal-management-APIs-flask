#  Travel Deal Management System (Backend)

A backend REST API built with **Python (Flask)** for managing travel deals. 

---
## Quick Preview

<img width="1815" height="899" alt="Screenshot from 2026-06-12 18-17-38" src="https://github.com/user-attachments/assets/95955922-ac0b-4255-9946-906bd97a0c26" />
<img width="1815" height="899" alt="Screenshot from 2026-06-12 18-18-02" src="https://github.com/user-attachments/assets/c5bcd399-29de-4e1d-8822-854558270f2e" />
<img width="1815" height="899" alt="Screenshot from 2026-06-12 18-18-32" src="https://github.com/user-attachments/assets/7256e7cd-f2d2-461e-a3e3-54161b7964f6" />

---

##  Postman Collection

Test all the available endpoints using the Postman collection below:

 **[Travel Deal Management API – Postman Collection](https://rezaparisa5-3329056.postman.co/workspace/Parisa-Reza's-Workspace~25280366-0849-4a23-831d-abb02d924f1a/collection/50965523-f11ad7f8-f2f7-4d8a-9eaf-b1e6368d73c8?action=share&creator=50965523)**

## Techstack


 
| Category            | Technology                                  |
|---------------------|----------------------------------------------|
| **Language**        | Python 3.12.3                                  |
| **Framework**       | Flask                                         |
| **Data Format**     | JSON                                          |
| **Database**        | SQLite
| **API Testing**     | Postman                                      |
| **Version Control** | Git & GitHub                                 |
| **Architecture**    | Modular (Routes → Services → Database) |
| **Environment**     | Python Virtual Environment (`venv`)          |
 






---

## Features

-  Add new travel deals via REST API
-  View all travel deals
-  View details of a single travel deal by ID
-  Robust input validation:
-  Proper JSON responses with meaningful messages
-  Appropriate HTTP status codes (200, 201, 400, 404, etc.)
-  Clean, modular project structure (routes / services / utils / database)
-  Business logic fully separated into the `services/` layer



---

##  API Endpoints Summary

| Method | Endpoint      | Description                  |
|--------|---------------|-------------------------------|
| POST   | `/deals`      | Add a new travel deal         |
| GET    | `/deals`      | Get all travel deals          |
| GET    | `/deals/<id>` | Get a single travel deal      |

---

##  Validation Rules

| Field         | Rule                                                |
|---------------|-----------------------------------------------------|
| `destination` | Cannot be empty                                     |
| `price`       | Must be a positive number                           |
| `rating`      | Must be between **1 and 5**                         |
| `travel_type` | Must be one of: `Budget`, `Luxury`, `Adventure`, `Family` |

---



##  Quick Setup & Installation

Follow the steps below to clone, set up, and run the project locally.

###  Clone the Repository
```bash
git clone https://github.com/Parisa-Reza/travel-deal-management-APIs-flask.git
cd travel-deal-management-APIs-flask
```

###  Create a Virtual Environment
```bash
python3 -m venv venv
```

Activate the virtual environment:

- **macOS / Linux**
  ```bash
  source venv/bin/activate
  ```

###  Install Dependencies
```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Run the Application
```bash
python3 app.py
```

By default, the server will start on:
```
http://127.0.0.1:5000
```



---

## License

This project was developed as part of the **W3 Engineers Ltd  Internship Assignment (Part 01)**
