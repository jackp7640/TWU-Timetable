from bs4 import BeautifulSoup
import requests

with open('sample_course_list.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')


#for tbody in soup.find_all('tbody'):
#	course = tbody.text
#	print(course)

for course_id in soup.find_all('a', id="pg0_V_ggCourses_sec2_row2_lnkCourse"):
	co_id = course_id.text
	print(co_id)