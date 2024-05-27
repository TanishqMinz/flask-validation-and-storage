from flask import Flask, request, render_template, redirect, url_for
import flask_login
from config import Config
from models import db, User, create_user, get_user_by_email
from verify import verify

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/form", methods=['GET'])
def show():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def main():
    errors = verify(request.form)
    if not errors:
        firstname = request.form["firstname"]
        email = f"{firstname}@email.com"
        user = get_user_by_email(email)
        if user:
            flask_login.login_user(user)
            return redirect(url_for('yay'))
        else:
            create_user(firstname, email)
            return redirect(url_for('newacc'))
    return render_template('form.html', errors=errors)

@app.route('/newacc')
def newacc():
    return render_template('newacc.html')

@app.route('/yay')
@flask_login.login_required
def yay():
    return render_template('yay.html')

@app.route('/users', methods=['GET'])
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)
