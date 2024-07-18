
# Flask Validation and Storage

## Description

This is a simple attempt I made at using form validation and data storage. It uses Flask to run the webpage, with common webpage forms including Register, Login, and Reset Password. It also includes logout and delete account features. It uses Flask-WTForms and Flask_login for data validation and session management. The details like username, email and password are stored in Flask-SQLAlchemy using Werkzeug for encrypted password storage.

## Technologies Used

- Flask
- Flask-WTForms
- Flask-login
- Flask-SQLAlchemy
- Werkzeug Security
- HTML
- Tailwind CSS

## Usage

1. Clone the repository:

    ```sh
    $ git clone https://github.com/TanishqMinz/flask-validation-and-storage/
    ```

2. Add a Python virtual environment to the root directory (same level as `app.py`):

    ```sh
    $ python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        With powershell as administrator:
        
        > Set-ExecutionPolicy RemoteSigned
        > .\venv\Scripts\Activate.ps1
        > Set-ExecutionPolicy Restricted
        ```

    - On macOS/Linux:

        ```sh
        $ source venv/bin/activate
        ```

4. Install all the Python dependencies:

    ```sh
    $ python -m pip install -r requirements.txt
    ```

5. Initialize the database:

    ```sh
    $ python init_db.py
    ```
    
6. Run the script:

    ```sh
    $ python app.py
    ```

7. Go to http://127.0.0.1:5000/
