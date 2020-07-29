from flask import render_template, url_for, flash, redirect
from localhost import app
from localhost.forms import RegistrationForm, LoginForm
from localhost.models import User, Post


posts = [
    {
        'author': 'Jorge Torre',
        'title': 'Primer Post',
        'content': 'Hola, este es mi primer thread en el foro. Gracias por todo. Un saludo.',
        'date_posted':'20 de Abril, 2018'
    },
    {
        'author': 'Ana María',
        'title': 'AnamaríaHD_YT',
        'content': 'Hola, mi nombre es Ana, subo gameplays de Call of Duty, síganme y les sigo.',
        'date_posted':' 21 de Abril, 2018',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =='password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
