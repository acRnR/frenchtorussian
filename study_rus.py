
from flask import Flask
from flask import url_for, render_template, request, redirect
from flask.ext.login import LoginManager


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(us_id):
    return User.query.get(int(us_id))


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(10))
    email = db.Column('email', db.String(50), unique=True, index=True)
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)



@app.route('/')
def index():
    if request.args:
        return redirect(pass)
    render_template('start_page.html')


@app.route('/signup')
def sign_up():
    if request.args:
        return redirect(pass)
    render_template('sign_up_page.html')


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/materials')
@login_required
def materials():
    render_template('materials_page.html')