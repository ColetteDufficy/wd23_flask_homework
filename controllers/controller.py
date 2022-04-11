from flask import render_template, request
from app import app

from models.event_list import events
from models.event import Event 

@app.route('/')
def index():
    return render_template("index.html", title="Home ")

@app.route('/events')
def list_events():
    return render_template("event_listing.html", title="Todays ", all_events = events)

@app.route('/events', methods=["POST"])
def add_event():
    ev_date = request.form['date']
    ev_event_name = request.form['title']
    ev_num_of_guests = request.form['guest numbers']
    ev_location = request.form['location']
    ev_descripton = request.form['description']
    ev_reoccuring = request.form['reoccuring']
    
        
    new_event = Event(ev_date, ev_event_name, ev_num_of_guests, ev_location, ev_descripton, ev_reoccuring)
    events.append(new_event)
    
    return render_template("event_listing.html", title="Todays ", all_events = events)