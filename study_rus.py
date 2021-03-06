#from datetime import datetime
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import session, request, flash, url_for, redirect, render_template, abort, g
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from flask.ext.login import LoginManager
#from flask.ext.login import login_user , logout_user , current_user , login_required


basedir = os.path.abspath(os.path.dirname(__file__))
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


def create_app(config_name):
    pass
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'


#@login_manager.user_loader
#def load_user(id):
 #   return User.query.get(int(id))


class User(UserMixin ,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)#'user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)#'username', db.String(20), unique=True), index=True)
    password_hash = db.Column(db.String(128))
    #password = db.Column('password', db.String(10))
    email = db.Column(db.String(64), unique=True, index=True)#'email', db.String(50), unique=True, index=True)
    #registered_on = db.Column('registered_on', db.DateTime)
    @property
    def password(self):
        raise ArithmeticError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    #def __init__(self, username, password, email):
     #   self.username = username
      #  self.password = password
       # self.email = email
        #self.registered_on = datetime.utcnow()

    #def is_authenticated(self):
     #   return True

    #def is_active(self):
     #   return True

    #def is_anonymous(self):
     #   return False

    #def get_id(self):
     #   return str(self.id)

    #def __repr__(self):
     #   return '<User %r>' % (self.username)


#@app.route('/register', methods=['GET', 'POST'])
#def register():
 #   if request.method == 'GET':
  #      return render_template('sign_up_page.html')
   # user = User(request.form['username'], request.form['password'], request.form['email'])
    #db.session.add(user)
    #db.session.commit()
    #flash('User successfully registered')
    #return redirect(url_for('login'))


#@app.route('/login', methods=['GET', 'POST'])
#def login():
 #   if request.method == 'GET':
  #      return render_template('start_page.html')
   # return redirect(url_for('index'))

#@app.route('/login', methods=['GET', 'POST'])
#def login():
 #   if request.method == 'GET':
  #      return render_template('start_page.html')
   # username = request.form['username']
    #password = request.form['password']
    #remember_me = False
    #if 'remember_me' in request.form:
     #   remember_me = True
    #registered_user = User.query.filter_by(username=username, password=password).first()
    #if registered_user is None:
     #   flash('Username or Password is invalid', 'error')
      #  return redirect(url_for('login'))
    #login_user(registered_user, remember=remember_me)
    #flash('Logged in successfully')
    #return redirect(request.args.get('next') or url_for('index'))


@app.route('/')
#@login_required
def index():
    return render_template('start_page.html')
 #   pass


@app.route('/materials')
#@login_required
def materials_pg():
    return render_template('materials_page.html')
    #pass


@app.route('/logout')
def logout():
    #logout_user()
    return redirect(url_for('index'))


@app.route('/user/<name>')
def user_pg(name):
    return render_template('profile_page.html', name=name)


#@app.before_request
#def before_request():
 #   g.user = current_user


if __name__ == '__main__':
    app.run(debug=True)
