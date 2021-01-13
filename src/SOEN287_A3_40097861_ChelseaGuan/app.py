import csv
import os
import bcrypt as bcrypt
from flask import Flask, render_template, redirect, url_for, session, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, DateField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length, EqualTo

app = Flask(__name__)
app.secret_key = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['USE_SESSION_FOR_NEXT'] = True


class ApplicationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[InputRequired()])
    radio_group = RadioField('Gender', validators=[InputRequired()], choices=[('Boy', 'Boy'), ('Girl', 'Girl'), ('Other', 'Other')], render_kw={'required': True})
    dob = DateField('Date of Birth', format='%Y-%m-%d')
    message = TextAreaField('Message')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    phone = StringField('Phone number', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(6)])
    password_repeat = PasswordField('Repeat password', validators=[InputRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Register')


class User(UserMixin):
    def __init__(self, first_name, last_name, phone, email, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
    def get_id(self):
        return (self.email)


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log in')

@login_manager.user_loader
def load_user(user_email):
    user = find_user(user_email)
    if user:
        user.password = None
    return user


def find_user(email):
    with open('data/accounts.csv') as f:
        for user in csv.reader(f):
            if not ''.join(user).strip():
                continue
            if (email == user[3]):
                return User(*user)
    return None


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/home')
def home():
    return index()


@app.route('/aboutus')
def aboutus():
    prefix = '/static/'
    with open('data/educators.csv') as f:
        doc_list_abt = list(csv.reader(f))[1:]
    return render_template("aboutus.html", doc_list_abt=doc_list_abt, prefix=prefix)


@app.route('/programs')
def programs():
    prefix = '/static/'
    with open('data/infant.csv') as f:
        doc_list_inf = list(csv.reader(f))[1:]
    with open('data/preschool.csv') as f:
        doc_list_pre = list(csv.reader(f))[1:]
    return render_template("programs.html", doc_list_inf=doc_list_inf, doc_list_pre=doc_list_pre, prefix=prefix)


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ApplicationForm()
    if form.validate_on_submit():
        with open('data/applications.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([form.full_name.data, form.radio_group.data, form.dob.data, form.message.data])
        return redirect(url_for('contact_response', full_name=form.full_name.data))
    return render_template('contact.html', form=form)


@app.route('/contact_response/<full_name>')
def contact_response(full_name):
    return render_template('contact_response.html', full_name=full_name)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = find_user(form.email.data)

        if not user:
            salt = bcrypt.gensalt()
            password = bcrypt.hashpw(form.password.data.encode(), salt)

            with open('data/accounts.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([form.first_name.data, form.last_name.data, form.phone.data, form.email.data, password.decode()])
            flash('Registered successfully.')
            return redirect(url_for('login'))
        else:
            flash('This email is already registered, please choose another one.')
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = find_user(form.email.data)
        if user and bcrypt.checkpw(form.password.data.encode(), user.password.encode()):
            login_user(user)
            next_page = session.get('next', '/')
            session['next'] = '/'
            return redirect(next_page)
        else:
            flash('Incorrect username/password!')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run()
