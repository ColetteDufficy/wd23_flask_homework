from flask import render_template
from app import app

from models.event_list import events
from models.event import Event 

@app.route('/')
def index():
    return "Welcome to my home page"

@app.route('/events')
def list_events():
    return render_template("index.html", title="Todays ", all_events = events)