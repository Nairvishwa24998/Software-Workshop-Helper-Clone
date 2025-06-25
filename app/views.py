
from datetime import datetime

from flask import render_template, redirect, url_for, flash, request, send_file, send_from_directory
from flask_socketio import SocketIO, emit
from app import app, socketio
from urllib.parse import urlsplit
import csv
import io

from app.dto import Student
from app.forms import StudentForm


current_que = []

# Used inside controller without web-sockets
def append_to_que(student):
    current_que.append(student)


def check_student_in_que(new_student):
    for student in current_que:
        if student.seat_number == new_student.seat_number:
            return True
    return False

def generate_seat_numbers():
    alphabets = "ABCDEFHIJKLMNOP"
    nums = [1, 2, 3, 4, 5, 6, 7]
    seats = []
    for alphabet in alphabets:
        for num in nums:
            seats.append(alphabet + str(num))
    return seats
seats = generate_seat_numbers()

@app.route("/", methods = ["GET", "POST"])
def home():
    form = StudentForm()
    if form.validate_on_submit():
        seat_number = form.seat_number.data
        name = form.name.data
        topic = form.topic.data
        current_student = Student(name, seat_number, topic, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        if form.seat_number.data not in seats:
            flash("Chosen seat number does not exist. Please choose one that exists", "danger")
            return render_template('home.html', title="SW2 Lab Helper", form = form)
        if check_student_in_que(current_student):
            flash("An assistance request associated with this seat number has already been made and is currently in the que. Please delete the existing request or ask one of the TA's to delete the request", "info")
            return render_template('home.html', title="SW2 Lab Helper",form = form)
        append_to_que(current_student)
        # emitting the updated que to the socket so it can be broadcasted to everyone
        # since sockets deal with JSON objects better, its ideal to convert Python Objects to serializable form
        socketio.emit('update_queue', {'queue': [vars(s) for s in current_que]})
        flash(f"An assistance request for seat number {seat_number} has been logged. Our TAs will reach out to you shortly","success")
    return render_template('home.html', title="SW2 Lab Helper",form = form)


@app.route("/queue")
def queue():
    return render_template("queue.html", current_que = current_que, title="SW2 Lab Helper")


# @socketio.on('add_student')
# def handle_add_student_to_que(data):
#     seat_number = data.get('seat_number')
#     if seat_number:
#         current_student = Student(name, seat_number, topic, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#         append_to_que(current_student)
#         append_to_que()
#         print(f"New student added: {seat_number}")
#         emit('update_queue', {'queue': queue}, broadcast=True)
#
# @socketio.on('remove_student')
# def handle_remove_student_from_que(data):
#     seat_number = data.get('seat_number')
#     if seat_number in queue:
#         queue.remove(seat_number)
#         print(f"Student removed: {seat_number}")
#         emit('update_queue', {'queue': queue}, broadcast=True)



# Error handlers
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Error handler for 403 Forbidden
@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html', title='Error'), 403

# Handler for 404 Not Found
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', title='Error'), 404

@app.errorhandler(413)
def error_413(error):
    return render_template('errors/413.html', title='Error'), 413

# 500 Internal Server Error
@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', title='Error'), 500


@socketio.on('connect')
def handle_connect():
    print('Client connected to WebSocket')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected from WebSocket')

@socketio.on_error()
def handle_error(e):
    print('WebSocket error:', e)