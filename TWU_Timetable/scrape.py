from bs4 import BeautifulSoup
import requests
import pandas as pd

dfs = pd.read_html('sample_course_list.html')
schedule_info = dfs[1]

num_courses = len(schedule_info)

courses_info = '{\
	"dataCheck":"69761aa6-de4c-4013-b455-eb2a91fb2b76",\
	"saveVersion":4,\
	"schedules":\
	[\
		{\
			"title":"",\
			"items":\
			['

list_of_colours = ['#FFE37D', '#C8F7C5', '#E08283', '#99CCCC', '#CC99CC', '#C4DA87', '#F7B891']
num             = ['001', '002', '003', '004', '005', '006', '007']


#repeat for every course
for x in range(0, num_courses):
	co_code = schedule_info.iloc[x][1]
	co_name = schedule_info.iloc[x][2]
	co_time = schedule_info.iloc[x][7]
	co_loc  = schedule_info.iloc[x][9]

	# formatting location
	formatted_co_loc = co_loc.split(" ")
	formatted_co_loc = formatted_co_loc[4] + " " + formatted_co_loc[8]

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
	
	if co_time_start_min == '00':
		co_time_start_min = '0'
	if co_time_end_min == '00':
		co_time_end_min = '0'

	M_TF = "false"
	T_TF = "false"
	W_TF = "false"
	R_TF = "false"
	F_TF = "false"
	S_TF = "false"
	U_TF = "false"

	formatted_co_time_day = list(co_time_day)
	for day in formatted_co_time_day:
		if day == 'M':
			M_TF = "true"

		elif day == 'T':
			T_TF = "true"

		elif day == 'W':
			W_TF = "true"

		elif day == 'R':
			R_TF = "true"

		elif day == 'F':
			F_TF = "true"

		elif day == 'S':
			S_TF = "true"

		elif day == 'U':
			U_TF = "true"




	courses_info += '{\
					"uid":"40975ca6-721f-401f-b4f6-9ca4dac7'+ num[x] +'c",\
					"type":"Course",\
					"title":"' + co_code + '",\
					"meetingTimes":\
					[\
						{\
							"uid":"1db48ca1-5dd8-4979-ab9f-d61e0884f' + num[x] + '",\
							"courseType":"",\
							"instructor":"",\
							"location":"' + formatted_co_loc + '",\
							"startHour":' + co_time_start_hr + ',\
							"endHour":' + co_time_end_hr + ',\
							"startMinute":' + co_time_start_min + ',\
							"endMinute":' + co_time_end_min + ',\
							"days":\
							{\
								"monday":' + M_TF + ',\
								"tuesday":' + T_TF + ',\
								"wednesday":' + W_TF + ',\
								"thursday":' + R_TF + ',\
								"friday":' + F_TF + ',\
								"saturday":' + S_TF + ',\
								"sunday":' + U_TF + '\
							}\
						}\
					],\
					"backgroundColor":"' + list_of_colours[x] + '"\
				},'

courses_info = courses_info[:-1]
courses_info += ']\
		}\
	]\
	,"currentSchedule":0\
}'

f = open("mySchedule.csmo","w+")
f.write(courses_info)