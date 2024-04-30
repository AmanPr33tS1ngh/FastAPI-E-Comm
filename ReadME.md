# Documentation

This repository contains a FastAPI project with several endpoints for managing products, orders, and user authentication.

## Endpoints

### 1. Get Products

- **Method**: `GET`
- **URL**: `/`
- **Description**: Retrieve a list of products.
- **Query Parameters**:
  - None
- **Request Headers**:
  - Authorization: Bearer {token}
- **Response**:
  - Status Code: 200 OK
  - Body: List of `ProductSchema` objects

### 2. Create Product

- **Method**: `POST`
- **URL**: `/create_product/`
- **Description**: Create a new product.
- **Request Body**:
  - `ProductSchema`
- **Request Headers**:
  - Authorization: Bearer {token}
- **Response**:
  - Status Code: 200 OK
  - Body: `ProductSchema` object

### 3. Get Orders

- **Method**: `GET`
- **URL**: `/orders/`
- **Description**: Retrieve a list of orders for a specific user.
- **Query Parameters**:
  - `user_id` (integer)
- **Request Headers**:
  - Authorization: Bearer {token}
- **Response**:
  - Status Code: 200 OK
  - Body: List of `OrderSchema` objects

### 4. Get Order

- **Method**: `GET`
- **URL**: `/order/`
- **Description**: Retrieve details of a specific order for a user.
- **Query Parameters**:
  - `user_id` (integer)
  - `order_id` (integer)
- **Request Headers**:
  - Authorization: Bearer {token}
- **Response**:
  - Status Code: 200 OK
  - Body: `OrderSchema` object

### 5. Create Order

- **Method**: `POST`
- **URL**: `/create_order/`
- **Description**: Create a new order.
- **Request Body**:
  - `OrderSchema`
- **Request Headers**:
  - Authorization: Bearer {token}
- **Response**:
  - Status Code: 200 OK
  - Body: `OrderSchema` object

### 6. Authenticate and Get Token

- **Method**: `POST`
- **URL**: `/api/token/`
- **Description**: Authenticate a user and generate an access token.
- **Request Body**:
  - `AuthSchema`
- **Response**:
  - Status Code: 200 OK
  - Body: JSON with access token (`"access_token"`)

### 7. Sign In

- **Method**: `POST`
- **URL**: `/signin/`
- **Description**: Sign in a user and return a token.
- **Request Body**:
  - `TokenSchema`
- **Response**:
  - Status Code: 200 OK
  - Body: JSON with access token (`"access_token"`)

### 8. Sign Up

- **Method**: `POST`
- **URL**: `/signup/`
- **Description**: Register a new user.
- **Request Body**:
  - `UserSchema`
- **Response**:
  - Status Code: 200 OK

## Usage

1. **Running the FastAPI Application**:

   - Make sure you have Python and FastAPI installed.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Start the FastAPI application:
     ```bash
     uvicorn main:app --reload
     ```

2. **Accessing the Endpoints**:
   - Use a tool like `curl` or `Postman` to send requests to the defined endpoints.
   - Ensure to include the required headers and request bodies as described in each endpoint's documentation.

## Example

```python
import requests

# Example: Get list of products
url = "http://localhost:8000/"
headers = {"Authorization": "Bearer <your_token_here>"}
response = requests.get(url, headers=headers)
print(response.json())
```
