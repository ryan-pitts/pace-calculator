#!/usr/bin/env python
""" This calculator determines pace, time, or distance. """
from datetime import time, timedelta

def get_input():
    values = {
        "time": "",
        "distance": 0
    }

    values["time"] = input("Enter expected time in hours, minutes, and seconds (HH:MM:SS):  ")
    values["distance"] = int(input("Enter distance in miles:  "))
    
    return values

def calculate_pace(user_values):
    secs_per_dist = convert_input_to_seconds(user_values.get("time")) / user_values.get("distance")
    return timedelta(seconds=secs_per_dist)

def convert_input_to_seconds(time_input):
    t = time.fromisoformat(time_input)
    secs = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds()
    return secs

user_values = get_input()
pace_time = calculate_pace(user_values)
print("Pace = " + str(pace_time) + " per mile")
