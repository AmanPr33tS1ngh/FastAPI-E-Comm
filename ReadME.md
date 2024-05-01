# FastAPI API Documentation

This repository contains a FastAPI project with various endpoints for user authentication, user profile management, product management, and order management.

## Endpoints

### 1. Authenticate and Get Token

- **Endpoint**: `/users/api/token/`
- **Method**: `POST`
- **Description**: Authenticate a user and obtain an access token.
- **Request Body**:
  ```{
    "username": "string",
    "hashed_password": "string"
- **Responses**:
  - `200`: Successful authentication, returns a JWT token.
  - `422`: Validation error with details.

### 2. Sign In

- **Endpoint**: `/users/signin/`
- **Method**: `POST`
- **Description**: Sign in a user and return a token.
- **Request Body**:
  ```{
    "token": "string"
- **Responses**:
  - `200`: Successful sign-in, returns a JWT token.
  - `422`: Validation error with details.

### 3. Sign Up

- **Endpoint**: `/users/signup/`
- **Method**: `POST`
- **Description**: Register a new user.
- **Request Body**:
  ```
    "name": "string",
    "username": "string",
    "email": "string",
    "hashed_password": "string"
- **Responses**:
  - `200`: Successful registration, returns a success message.
  - `422`: Validation error with details.

### 4. Get User Profile

- **Endpoint**: `/users/profile/`
- **Method**: `GET`
- **Description**: Retrieve user profile details.
- **Request Headers**:
  - `token`: User's JWT token.
- **Responses**:
  - `200`: Successful response, returns user profile details.
  - `422`: Validation error with details.

### 5. Update User Profile

- **Endpoint**: `/users/update_profile/`
- **Method**: `PUT`
- **Description**: Update user profile information.
- **Request Headers**:
  - `token`: User's JWT token.
- **Request Body**:
  ```
    "name": "string",
    "username": "string",
    "email": "string",
    "hashed_password": "string"
- **Responses**:
  - `200`: Successful update, returns updated user profile details.
  - `422`: Validation error with details.

### 6. Get Orders

- **Endpoint**: `/orders/`
- **Method**: `GET`
- **Description**: Retrieve a list of orders.
- **Request Headers**:
  - `token`: User's JWT token.
- **Responses**:
  - `200`: Successful response, returns a list of order objects.
  - `422`: Validation error with details.

### 7. Create Order

- **Endpoint**: `/orders/`
- **Method**: `POST`
- **Description**: Create a new order.
- **Request Headers**:
  - `token`: User's JWT token.
- **Request Body**:
  ```
    "quantity": 0,
    "user_id": 0,
    "product_id": 0,
    "order_amount": 0,
    "transaction_id": "string",
    "is_delivered": true,
    "created_at": "string"
- **Responses**:
  - `200`: Successful order creation, returns the created order object.
  - `422`: Validation error with details.

### 8. Get Order Details

- **Endpoint**: `/orders/{order_id}/`
- **Method**: `GET`
- **Description**: Retrieve details of a specific order.
- **Path Parameters**:
  - `order_id`: ID of the order.
- **Request Headers**:
  - `token`: User's JWT token.
- **Responses**:
  - `200`: Successful response, returns details of the specified order.
  - `422`: Validation error with details.

**Running the FastAPI Application**:
   - Make sure you have Python and FastAPI installed.
   - Install dependencies:
     pip install -r requirements.txt
   - Start the FastAPI application:
     uvicorn main:app --reload

## Dependencies

- Python 3.7+
- FastAPI
- SQLAlchemy (for database operations)
- uvicorn (for running the FastAPI application)


