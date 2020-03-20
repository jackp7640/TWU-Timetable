import sys
from request import request
from scrape import scrape
from make_table import make_table

def get_table():
	username = sys.argv[1]
	password = sys.argv[2]

	request(username, password)
	scrape("twu_website.html")
	make_table()


get_table()