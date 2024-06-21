This project is a FastAPI application that interacts with a SQL database to provide a set of APIs.

Features

1. Fast and efficient API built with FastAPI
2. SQL database integration

Requirements

1. Python 3.x
2. FastAPI
3. A SQL database (MySQL)

Installation

1. Clone the repository:
   git clone https://github.com/krna-sharma/telecom.git
   cd yourproject*

2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

Running the Application
1. uvicorn main:app --reload
   The application will be available at `http://127.0.0.1:8000

API Endpoints

#### Get all items

- **URL**: `/cust_details`
- **Method**: `GET`
- **Description**: Retrieves a json of all customer name and id.


#### Register a new customer

- **URL**: `/register`
- **Method**: `POST`
- **Description**: Creates a new customer.
- **Body**:
    ```json
    {
  	"name": "string",
  	"dob": "string",
  	"email": "string",
  	"aadhaar": "string",
  	"number": "string"
    }
    ```

#### Change Plan

- **URL**: `/change_plan`
- **Method**: `POST`
- **Description**: Update customer plan.
- **Body**:
    ```json
    {
  	"email": "string",
  	"new_plan_name": "string"
    }

    ```