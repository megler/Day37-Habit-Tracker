# habitTracker.py
#
# Python Bootcamp Day 37 - Habit Tracker
# Usage:
#      A habit tracker using Pixela. See README for walkthrough.
#
# Marceia Egler December 8, 2021

import os
import requests
from datetime import datetime as dt, timedelta
from dotenv import load_dotenv


load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv("api")
USERNAME = os.getenv("user")
GRAPH_ENDPOINT = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "walking1"
today = dt.now().strftime("%Y%m%d")

# change days= to however many days you want to look back
previous_days = dt.now() - timedelta(days=1)
previous_days_str = previous_days.strftime("%Y%m%d")


def create_user():
    create_user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    r = requests.post(url=pixela_endpoint, json=create_user_params)

    return r.text


def create_graph(name: str, unit: str, type: str, color: str, timezone: str):

    token = {
        "X-USER-TOKEN": TOKEN,
    }
    graph_params = {
        "id": GRAPH_ID,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color,
        "timezone": timezone,
    }

    r = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=token)


def add_pixel(quantity: str):
    token = {
        "X-USER-TOKEN": TOKEN,
    }
    add_day_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    add_day_graph_params = {
        "date": today,
        "quantity": quantity,
    }

    r = requests.post(
        url=add_day_graph_endpoint, json=add_day_graph_params, headers=token
    )
    return r.text


def update_pixel(quantity: str, when: str):
    token = {
        "X-USER-TOKEN": TOKEN,
    }
    update_graph_endpoint = (
        f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{when}"
    )
    update_graph_params = {
        "quantity": quantity,
    }

    r = requests.put(
        url=update_graph_endpoint, json=update_graph_params, headers=token
    )
    return r.text


def delete_pixel(when: str, quantity: str):
    token = {
        "X-USER-TOKEN": TOKEN,
    }
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{when}"

    delete_graph_params = {
        "quantity": quantity,
    }

    r = requests.delete(
        url=delete_endpoint, json=delete_graph_params, headers=token
    )
    return r.text


# create_user(TOKEN, USERNAME)
# create_graph("Walking Tracker", "steps", "int", "ajisai", "US/Eastern")
# add_pixel("1000")
# update_pixel("500", previous_days_str)
# delete_pixel(previous_days_str, "500")
