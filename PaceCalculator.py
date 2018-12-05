#!/usr/bin/env python
""" This calculator determines pace, time, or distance. """

def get_input():
    values = {
        "time": 0,
        "distance": 0
    }

    values["time"] = int(input("Enter expected time in minutes:  "))
    values["distance"] = int(input("Enter distance in miles:  "))
    
    return values

def calculate_pace(user_values):
    return user_values.get("time") / user_values.get("distance")

user_values = get_input()
print("Pace = " + str(calculate_pace(user_values)) + " mins/mile")
