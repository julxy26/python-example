# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import string
import random
import subprocess
import sys
import smtplib
from string import Template
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
import json
from pathlib import Path
import time
from datetime import datetime, timedelta

# SQLite
movies = json.loads(Path("movies.json").read_text(
    encoding="utf8"))  # fetch data from file

with sqlite3.connect("db.sqlite3") as connect:  # create database "db.sqlite3"
    command = "INSERT INTO Movies VALUES(?, ?, ?)"  # ? => placeholders
    for movie in movies:  # iterating through movies
        # insert tuple into Movies table
        connect.execute(command, tuple(movie.values()))
    connect.commit()  # written to database


with sqlite3.connect("db.sqlite3") as connect:
    command = "SELECT * FROM Movies"
    cursor = connect.execute(command)
    # for row in cursor: # returns each row in a tuple
    # print(row)
    movies = cursor.fetchall()  # returns everything as a tuple in a list
    # print(movies)


time.time()  # returns in seconds counting from 1.1.1970
# datetime => point in time
# timedelta => duration
dt = datetime(2023, 2, 26, 9, 22, 54)  # y, m, d, hh, mm, ss
dt2 = datetime.now() + timedelta(days=2, seconds=1000)
# converts string into date time object
dt3 = datetime.strptime("2023/2/1", "%Y/%m/%d").date()
# converts date time object into string
dt4 = dt2.strftime("%Y/%m/%d")
# converts timestamp into date time object
dt5 = datetime.fromtimestamp(time.time())
formatted = f"{dt.year}/{dt.month}"


duration = dt - dt2
print(duration)  # 9 days, 23:11:19.501059
print("timedelta", dt2)  # 2023-02-18 11:48:46.800377
print("days", duration.days)  # days 9
print("seconds", duration.seconds)  # seconds 83479
print("total", duration.total_seconds())  # total 861079.501059


# random generator
random.random()  # float number
random.randint(1, 100)  # integer between 1-100
random.choice([1, 2, 3, 4, 5])  # random number from array
# .join => into one string with no separator, string => all letters and digits, k => amount
"".join(random.choices(string.ascii_letters + string.digits, k=4))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)  # returns random order

# open web browser
# => import webbrowser
# webbrowser.open("https://www.homepage.com")

# send emails
template = Template(Path("template.html").read_text(encoding="UTF-8"))

message = MIMEMultipart()
message["from"] = "Max Mustermann"
message["to"] = "sample@gmail.com"
message["subject"] = "sample email"
# takes dictionary or keyword argument
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))  # default "plain" text
# MIMEImage takes image file in binary
message.attach(MIMEImage(Path("image-name.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # greets server
    smtp.starttls()  # puts smtp connection in tls(transport layer security) mode => encryption
    smtp.login("sample@gmail.com", "testtest123")
    smtp.send_message(message)


# command-line arguments
if len(sys.argv) == 1:
    # print("USAGE: python app.py <password>")
    pass
else:
    # password = sys.argv[1]
    # print("password: ", password)
    pass


# run external programs
# takes commands in array of strings
# running child processes => run external python file
# => ["python", "file_name.py"] // stored in different memory space, does not share same variables
try:
    completed = subprocess.run(
        # check => raise exception when there's an error
        ["ls", "-l"], capture_output=True, text=True, check=True)
    print("args", completed.args)  # arguments listed above
    print("returncode", completed.returncode)  # if not 0 => error
    print("stderr", completed.stderr)  # standard error
    print("stdout", completed.stdout)  # standard output
except subprocess.CalledProcessError as ex:
    print(ex)
