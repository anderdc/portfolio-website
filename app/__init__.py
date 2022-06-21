from flask import Flask, render_template
import json

app = Flask(__name__)

#parse files w/ lists of json's
with open('app/static/data/work.json') as file:
    data = json.load(file)
    work_d = data.copy()

with open('app/static/data/hobbies.json') as file:
    data = json.load(file)
    hobbies_d = data.copy()

with open('app/static/data/education.json') as file:
    data = json.load(file)
    education_d = data.copy()

#flask backend
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/work')
def work():
    return render_template('work.html', work = work_d)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', hobbies = hobbies_d)

@app.route('/education')
def education():
    return render_template('education.html', education = education_d)

@app.route('/travel')
def travel():
    return render_template('travel.html')