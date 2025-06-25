from datetime import datetime


class Student:
    def __init__(self, name: str, seat_number: int, topic: str,time_of_request: str):
        self.name = name
        self.seat_number = seat_number
        self.topic = topic
        self.time_of_request = time_of_request

    def __str__(self):
        return f"Student(name={self.name}, seat_number={self.seat_number}, topic={self.topic}, time_of_request = {self.time_of_request})"
