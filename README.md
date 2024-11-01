
# Flask Validation and Storage

## Description

This is a simple attempt I made at using form validation and data storage. It uses Flask to run the webpage, using Flask-Login and Flask-WTForms for form validation and session management. The users details are stored in an SQLAlchemy database, with passwords stored in encrypted format for safety. It also features logout and delete functions, which are only available to a signed in user.
## Technologies Used

- Flask
- Flask-Login
- Flask-WTForms
- Flask-SQLAlchemy
- Werkzeug.security
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

5. Install Tailwind CSS and configure it:

    ```sh
    $ npm install tailwindcss
    $ npx tailwindcss init
    ```

    - Make sure tailwind.config.js looks like this :

    ```sh
        /** @type {import('tailwindcss').Config} */
        module.exports = {
        mode: "jit",
        content: ["./templates/**/*.html"],
        theme: {
            extend: {},
        },
        plugins: [],
        }
    ```

    - Create a folder static with the file styles.css

    - Run this script :

    ```sh
        npx tailwindcss -i src/styles.css -o static/styles.css --watch
    ```

6. Initialize the database:

    ```sh
    $ python init_db.py
    ```
    
7. Run the script:

    ```sh
    $ python app.py
    ```

8. Go to http://127.0.0.1:5000/
