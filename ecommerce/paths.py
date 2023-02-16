""" working with files and directories (path class)"""

from pathlib import Path
from zipfile import ZipFile
import csv
import json

# absolute path for windows
Path(r"C:\\projects\python-example")

# absolute path for mac/linux
Path("/usr/local/bin")

# current folder
Path()

# relative path
Path("ecommerce/__init__.py")

# combine path objects/string
path = Path() / "ecommerce" / "__init__.py"

# returns to home directory of current user
Path.home()


path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
path.mkdir()
path.rmdir()
path.rename("ecommerce2")
print(path.name)
# file name without extension
print(path.stem)
# get extension
print(path.suffix)
# get parent folder
print(path.parent)
# create new path object with different name and extension
path = path.with_name("file.txt")
path = path.with_suffix(".txt")
# path with absolute value
path.absolute()
# get list of files in directory
path.iterdir()  # => returns generater object (new value everytime)

# iterates through objects in path
# => returns only directories in PosixPath(mac) / WindowsPath(windows)
paths = [p for p in path.iterdir() if p.is_dir()]
# search for patterns and recursively
py_files = list(p for p in path.glob("*.py"))
# recursively
py_files = list(p for p in path.glob("**/*.py"))
py_files = list(p for p in path.rglob("*.py"))


# with ZipFile("files.zip", "w") as zip_file: # "w" => write mode
# find all files in current directory and its children
#  for path in Path("ecommerce").rglob("*.*"):
#       zip_file.write(path)


with ZipFile("files.zip") as zip_file:
    print(zip_file.namelist())  # get name of files
    info = zip_file.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    # copy files and put as zip files in "extract" directory
    zip_file.extractall("extract")


# CSV files => Comma Separated Values
with open("data.csv", "w", encoding="utf8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["transaction_id", "product_id", "product_price"])
    writer.writerow([97, 1, 10])
    writer.writerow([98, 2, 25])
    writer.writerow([99, 3, 15])


with open("data.csv", encoding="utf8") as csv_file:
    reader = csv.reader(csv_file)
    # print(list(reader)) # list with listed data
    for row in reader:
        print(row) # each row in a separate list


# json files
movies = [
    {"id": 1, "title": "Spirited Away", "rating": 9},
    {"id": 2, "title": "Howl's Moving Castle", "rating": 10},
    {"id": 3, "title": "Princess Mononoke", "rating": 8}
]

json_data = json.dumps(movies) # converts dictionary into json

Path("movies.json").write_text(json_data, encoding="utf8") # creating json file with data

# when using external data
path = Path("movies.json").read_text(encoding="utf8") # creating json file with data
movies = json.loads(path) # converts objects to array of dictionaries
print(movies[1]["title"])
