# pypi.org
# pip install package_name
# pip install package_name==version (ex.: 2.9.0) // earlier version
# pip install package_name==version* (ex.: 2.* or 2.9.*) // latest compatible version
# pip install package_name~=version (ex.: 2.9.0) // latest compatible version
# access virtual environment => pipenv shell
# get path to VE => pipenv --venv
# in settings.json paste python path
# change to correct environment in vscode


# if VE does not exist on local machine
# => pipenv install // to install all dependencies
# for exact version => pipenv install --ignore-pipfile
import requests
from bs4 import BeautifulSoup

response = requests.get("https://dog.ceo/api/breeds/list", timeout=None)
json_res = response.json()
first_five = json_res["message"][:5]
print(first_five)

# every breed in the list
for breed in json_res["message"]:
    print(breed)

# pipenv graph => see all dependecies and their versions
# update dependencies => pipenv update --outdated


# api key => store in config.py
# reference with import config
# put config.py in .gitignore


# web scraping
# get all questions from the first page
response = requests.get(
    "https://stackoverflow.com/questions", timeout=None)  # fetch
soup = BeautifulSoup(response.text, "html.parser")  # parse the response
# get the elements with the class name
questions = soup.select(".s-post-summary")
# iterate through all elements
for question in questions:
    # print all questions with the class name
    print(question.select_one(".s-link").getText())
    # print votes
    print((question.select_one(".s-post-summary--stats-item-number").getText()))
