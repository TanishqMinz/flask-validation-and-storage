
# Flask Validation and Storage

## Description

This is a simple attempt I made at using form validation and data storage. It uses Flask to run the webpage, with some validation (e.g., names must be only alphabets with no spaces). It then stores the first name, along with an email in the format 'firstname@email.com' in an SQLAlchemy database. When submitting a valid form, it takes the user to either a logged-in screen or an account-made screen, depending on whether the email with the same name exists in the database or not. You can also view the already created users names and email, update their names, and delete the users

## Technologies Used

- Regular Expressions
- Flask
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

7. Go to http://127.0.0.1:5000/form
