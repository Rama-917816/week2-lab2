# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build RESTful APIs using the FastAPI framework in Python. Learn to create endpoints, handle HTTP requests and responses, and implement basic API functionality.

## 📝 Tasks

### 🛠️	Set Up FastAPI Project

#### Description
Install FastAPI and create a basic project structure with a simple "Hello World" endpoint.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a FastAPI app instance
- Define a GET endpoint at "/" that returns a JSON response with a greeting message
- Run the server and verify the endpoint works


### 🛠️	Create CRUD Endpoints for Items

#### Description
Implement Create, Read, Update, Delete (CRUD) operations for a simple "item" resource using different HTTP methods.

#### Requirements
Completed program should:

- Define a Pydantic model for an Item with fields like id, name, and description
- Create a POST endpoint to add new items
- Create a GET endpoint to retrieve all items or a specific item by ID
- Create a PUT endpoint to update an existing item
- Create a DELETE endpoint to remove an item
- Use in-memory storage (list or dict) for items


### 🛠️	Add Request Validation and Error Handling

#### Description
Enhance the API with input validation, error handling, and documentation.

#### Requirements
Completed program should:

- Use Pydantic models for request/response validation
- Handle common errors (e.g., item not found) with appropriate HTTP status codes
- Add API documentation using FastAPI's automatic docs
- Include example requests and responses in the code comments