from flask import Flask, render_template, request, redirect, url_for,Response
import json
import os 
from peewee import *            #for interacting w/ mysql database
import datetime as dt
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv
load_dotenv('.env')
#from jinja2 import Environment, FileSystemLoader

#database integration
#creates a database object from .env file
# if os.getenv("TESTING") == "true":
# 	print("Running in test mode")
# 	db = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
# else:
# 	db = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
# 		user= os.getenv("MYSQL_USER"),
# 		password=os.getenv("MYSQL_PASSWORD"),
# 		host=os.getenv("MYSQL_HOST"),
# 		port=3306)
# print(db)

# class TimelinePost(Model):
#     name = CharField()
#     email = CharField()
#     content = TextField()
#     created_at = DateTimeField(default = dt.datetime.now)

#     class Meta:
#         database = db
# db.connect()
# db.create_tables([TimelinePost])

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
app = Flask(__name__)
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

# @app.route('/timeline')
# def timeline():
#     return render_template('timeline.html', posts=TimelinePost.select().order_by(TimelinePost.created_at.desc()))

# #for posting and retrieving database info
# @app.route('/api/timeline_post', methods=['POST'])
# def post_timeline_post():
#     if 'name' not in request.form:
#         return Response("Invalid name", status=400)
#     if 'email' not in request.form or '@' not in request.form['email']:
#         return Response("Invalid email", status=400)
#     if 'content' not in request.form or request.form['content'] == '':
#         return Response("Invalid content", status=400)

#     name = request.form['name']
#     email = request.form['email']
#     content = request.form['content']
#     timeline_post = TimelinePost.create(name=name, email=email, content=content)
#     return model_to_dict(timeline_post)

# @app.route('/api/timeline_post', methods=['GET'])
# def get_timeline_post():
#     return {
#         'timeline_posts': [model_to_dict(post) for post in TimelinePost.select().order_by(TimelinePost.created_at.desc())],
#     }

# #method to delete a post w a certain id
# @app.route('/api/timeline_post', methods=['DELETE'])
# def delete_timeline_post():
#     id = request.form['id']
#     try:
#         timelinepost = TimelinePost.get_by_id(id)
#         timelinepost.delete_instance()
#         return Response(f'post with id {id} was deleted', status=200)
#     except DoesNotExist as e:
#             return Response(f'post with id {id} not found.', status=400)
