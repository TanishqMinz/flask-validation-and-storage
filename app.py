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
    else:
        return render_template('form.html', errors=errors)

@app.route('/newacc')
def newacc():
    return render_template("form.html")

@app.route('/yay')
@flask_login.login_required
def yay():
    return render_template('yay.html')

@app.route('/users', methods=['GET'])
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/update_user', methods=['POST'])
def update_user():
    user_id = request.form.get('user_id')
    firstname = request.form.get('firstname')

    user = User.query.get(user_id)
    if user:
        user.firstname = firstname
        db.session.commit()

    return redirect(url_for('show_users'))

@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.form.get('user_id')
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('show_users'))

if __name__ == "__main__":
    app.run(debug=True)
