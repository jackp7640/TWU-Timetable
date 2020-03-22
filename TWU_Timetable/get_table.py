import sys
from getpass import getpass
from request import request
from scrape import scrape
from make_table import make_table

def get_table():
	username = input("Username: ")
	password = getpass()

	selected_term = request(username, password)
	scrape("twu_website.html")
	make_table(selected_term)


get_table()