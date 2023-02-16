# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import sqlite3
import json
from pathlib import Path

#SQLite
movies = json.loads(Path("movies.json").read_text(encoding="utf8")) # fetch data from file

with sqlite3.connect("db.sqlite3") as connect: # create database "db.sqlite3"
    command = "INSERT INTO Movies VALUES(?, ?, ?)" # ? => placeholders
    for movie in movies: # iterating through movies
        connect.execute(command, tuple(movie.values())) # insert tuple into Movies table
    connect.commit() # written to database


with sqlite3.connect("db.sqlite3") as connect:
    command = "SELECT * FROM Movies"
    cursor = connect.execute(command)
    # for row in cursor: # returns each row in a tuple
        # print(row)
    movies = cursor.fetchall() # returns everything as a tuple in a list
    # print(movies)
