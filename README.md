# FastAPI MVC Web Application :  Backend Developer Test

This is a web application built using FastAPI following the MVC (Model-View-Controller) design pattern. It provides endpoints for user authentication, posting, and retrieval, interfacing with a MySQL database using SQLAlchemy for ORM.

## Project Structure

- **app/**: Contains the main application code.
  - **routes/**: Defines controllers for handling HTTP requests.
  - **models/**: Contains SQLAlchemy models representing database tables.
  - **schemas/**: Pydantic models for request/response validation.
  - **core/**: Business logic layer for handling application tasks.
  - **main.py**: Entry point for running the FastAPI application.
- **requirements.txt**: Lists all Python dependencies for the project.
- **README.md**: Documentation explaining the project and how to run it.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <root>
    ```

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # for Linux/macOS
    # or
    .\venv\Scripts\activate   # for Windows
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set up your MySQL database and configure the connection string in `app/__init__.py`.
2. Run the FastAPI application:

    ```bash
    uvicorn app.main:app --reload
    ```

3. Access the API documentation at `http://localhost:8000/docs`.

## Endpoints

- **Signup**: `POST /signup`
  - Creates a new user account.
  - Request body:
    ```json
    {
        "email": "user@example.com",
        "password": "password123"
    }
    ```
  - Returns a token upon successful signup.

- **Login**: `POST /login`
  - Authenticates a user and returns a token.
  - Request body:
    ```json
    {
        "email": "user@example.com",
        "password": "password123"
    }
    ```
  - Returns a token upon successful login.

- **AddPost**: `POST /posts`
  - Adds a new post for the authenticated user.
  - Requires a valid authentication token.
  - Request body:
    ```json
    {
        "text": "This is a new post."
    }
    ```
  - Returns the ID of the newly created post.

- **GetPosts**: `GET /posts`
  - Retrieves all posts for the authenticated user.
  - Requires a valid authentication token.
  - Implements response caching for up to 5 minutes.
  - Returns a list of posts.

- **DeletePost**: `DELETE /posts/{post_id}`
  - Deletes the specified post for the authenticated user.
  - Requires a valid authentication token.
  - Returns a success message upon successful deletion.

