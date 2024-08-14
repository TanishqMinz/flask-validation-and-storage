from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, LoginManager, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from models import User, db
from forms import LoginForm, RegistrationForm, PasswordResetForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)  

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def start():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))  
        else:
            flash('Login failed. Check your email and password.')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))
    elif request.method == 'POST':  
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Error in {getattr(form, field).label.text}: {error}')
    return render_template('register.html', form=form)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.new_password.data):
                flash('New password cannot be the same as the old password.')
            else:
                hashed_password = generate_password_hash(form.new_password.data, method='pbkdf2:sha256')
                user.password = hashed_password
                db.session.commit()
                flash('Your password has been updated!', 'success')
                return redirect(url_for('login'))
        else:
            flash('No account found with that email.')
    return render_template('password.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    user_id = current_user.id
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        logout_user()  
        return redirect(url_for('login'))
    else:
        flash('Failed to delete account. Please try again.')
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
