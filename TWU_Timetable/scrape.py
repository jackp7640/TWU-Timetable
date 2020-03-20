from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

def scrape(html_file):

	dfs = pd.read_html(html_file)
	schedule_info = dfs[1]

	num_courses = len(schedule_info)
	earliest_start = "2399"
	latest_end     = "0"

	info = ""

	#repeat for every course
	for x in range(0, num_courses):
		co_code = schedule_info.iloc[x][1]
		co_name = schedule_info.iloc[x][2]
		co_time = schedule_info.iloc[x][7]
		co_loc  = schedule_info.iloc[x][9]

		# formatting location
		formatted_co_loc = co_loc.split(" ")
		formatted_co_loc = formatted_co_loc[4] + " " + formatted_co_loc[8]
		co_loc = formatted_co_loc

		# formatting time
		formatted_co_time = co_time.split(" ")
		if "PM" in formatted_co_time:
			co_time_day   = formatted_co_time[0]
			co_time_start = formatted_co_time[2]
			co_time_end   = formatted_co_time[5]
			co_time_AM_PM = formatted_co_time[3]
		else:
			co_time_day   = formatted_co_time[0]
			co_time_start = formatted_co_time[2]
			co_time_end   = formatted_co_time[4]
			co_time_AM_PM = formatted_co_time[5]

		# convert 12 hr time to 24 hr time
		if co_time_AM_PM == "PM" and co_time_start != '12:00':
			co_time_start_24 = pd.to_datetime(co_time_start+"PM").strftime('%H:%M')
			co_time_end_24   = pd.to_datetime(co_time_end+"PM").strftime('%H:%M')
		else:
			co_time_start_24 = co_time_start
			co_time_end_24   = co_time_end

		formatted_co_time_start = co_time_start_24.split(":")
		formatted_co_time_end = co_time_end_24.split(":")

		co_time_start_hr  = formatted_co_time_start[0]
		co_time_start_min = formatted_co_time_start[1]
		co_time_end_hr    = formatted_co_time_end[0]
		co_time_end_min   = formatted_co_time_end[1]
		co_time_start_AM_or_PM = ''
		co_time_end_AM_or_PM   = ''

		if int(co_time_end_hr) > 12:
			co_time_end_AM_or_PM = 'PM'
		else:
			co_time_end_AM_or_PM   = 'AM'

		if int(co_time_start_hr) > 12:
			co_time_start_AM_or_PM = 'PM'
		else:
			co_time_start_AM_or_PM   = 'AM'

		a = co_time_start_hr + co_time_start_min
		b = co_time_end_hr + co_time_end_min
		time1 = datetime.strptime(a,"%H%M") # convert string to time
		time2 = datetime.strptime(b,"%H%M") 
		diff = time2 - time1
		duration = diff.total_seconds()/60    # seconds to mins 

		print("duration of class: {}".format(duration))
		print("this course # is: {}".format(x))


		list_of_co_day = list(co_time_day)
		for day in list_of_co_day:
			if day == 'M':
				list_of_co_day[list_of_co_day.index(day)] = '1'

			elif day == 'T':
				list_of_co_day[list_of_co_day.index(day)] = '2'
		
			elif day == 'W':
				list_of_co_day[list_of_co_day.index(day)] = '3'
		
			elif day == 'R':
				list_of_co_day[list_of_co_day.index(day)] = '4'

			elif day == 'F':
				list_of_co_day[list_of_co_day.index(day)] = '5'

			elif day == 'S':
				list_of_co_day[list_of_co_day.index(day)] = '6'

			elif day == 'U':
				list_of_co_day[list_of_co_day.index(day)] = '7'



		print(co_code)
		print(co_name)
		print(list_of_co_day)
		print(co_time_start_24 + " - " + co_time_end_24)
		print(co_loc)

		start = co_time_start_hr + co_time_start_min
		end   = co_time_end_hr + co_time_end_min

		if int(start) < int(earliest_start):
			earliest_start = start

		if int(end) > int(latest_end):
			latest_end = end

		for day in list_of_co_day:
			info += str(x) + "/" + co_code + "/" + co_name + "/" + day + "/" \
					+ co_time_start_hr + "/" + co_time_start_min + "/" + co_time_end_hr + "/" + co_time_end_min  \
					+ "/" + str(duration) + "/" + co_loc + "/" + co_time_start_AM_or_PM + "/" + co_time_end_AM_or_PM +"/" +"\n" 
	 


	f = open("mySchedule.txt","w+")
	f.write(info)
	 
	f = open("startend.txt","w+")
	f.write(earliest_start + "/" + latest_end)
		# WHAT NEEDS TO BE IN TXT FILE
		# 1) FOR EVERY COURSE
		# 	a) co_code
		# 	b) co_name
		# 	c) co_time_day
		# 	d) co_time_start (12 hr)
		# 	e) co_time_end (12 hr)
		# 	f) co_loc
		# 2) earliest_start
		# 3) latest_end

