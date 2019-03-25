from flask import Flask, render_template, request, json, redirect, session
from flask import Markup
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
import requests

app = Flask(__name__)
app.config["DEBUG"] = False
app.config['SECRET_KEY'] = "JutzX21JOBqOdxlCV8xqqnxD"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
  def __init__(self,id):
    self.id = id

@app.route('/')
@login_required
def index():
    return render_template('index.html', title='Guanlin Pythonanywhere')

@app.route("/food")
def food():
    return render_template('food.html')

@app.route("/route")
def route():
    return render_template('route.html')

@app.route("/note1")
def note1():
    return render_template('note1.html')

@app.route("/note2")
def note2():
    return render_template('note2.html')

@app.route("/note3")
def note3():
    return render_template('note3.html')

@app.route("/map1")
def map1():
    return render_template('map1.html')

@app.route("/map2")
def map2():
    return render_template('map2.html')

@app.route("/map3")
def map3():
    return render_template('map3.html')

@app.route("/table")
def table():

   r = requests.get('https://api.airtable.com/v0/appnz0jma5BilSbeD/%E6%99%AF%E7%82%B9?api_key=key0eGGPlI2X82Vz3')
   dict = r.json()
   dataset = []
   for i in dict['records']:
           dict = i['fields']
           dataset.append(dict)

   return render_template('table.html', entries=dataset)

@app.route("/chart")
def chart():

    r = requests.get('https://api.airtable.com/v0/appWnfZpg7qUmwgeU/uesr_login?api_key=key0eGGPlI2X82Vz3')
    dict1 = r.json()
    dict2 = {}
    dataset = []
    name_list = []
    total_entries_list = []
    for i in dict1['records']:
         dict2 = i['fields']
         dataset.append(dict2)
    for item in dataset:
        name_list.append(item.get('Name'))
        total_entries_list.append(item.get('TotalCreds'))
    return render_template('chart.html', entries = zip(name_list, total_entries_list))

@app.route("/login")
def login():
    message = 'Please login in first. '
    return render_template('login.html', message=message)

@app.route("/process",methods=['POST'])
def process():
    username = request.form['username']
    password = request.form['password']
    if  password == 'password':
        login_user(User(1))
        message = "Dear " + username + ", welcome to Guanlin's pages. Your login has been granted. "
        return render_template('index.html', message=message)
    message = 'wrong password!'
    return render_template('login.html',message=message)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    message = 'Thanks for logging out. '
    return render_template('login.html',message=message)

if __name__ == '__main__':
   app.run(debug = True)
