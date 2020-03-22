##### TO DO #################################
# 1) change colours based on course_id - FIXED
# 2) retractable timetable size - FIXED
# 3) fix width of each item on the timetable - FIXED
# 40 fix the text position - FIXED
#############################################


import matplotlib.pyplot as plt
import math
import os

def make_table(selected_term):

    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    colors=['pink', 'lightgreen', 'lightblue', 'wheat', 'salmon', 'slateblue', 'slategrey']
    start_index = 0
    end_index   = 0

    time_compare_list = [
                        800, 815, 830, 845, 900, 915, 930, 945, 1000, 1015, 1030, 1045, 1100, 1115, 1130, 1145, 1200, 1215, 1230, 1245, 
                        1300, 1315, 1330, 1345, 1400, 1415, 1430, 1445, 1500, 1515, 1530, 1545, 1600, 1615, 1630, 1645,
                        1700, 1715, 1730, 1745, 1800, 1815, 1830, 1845, 1900, 1915, 1930, 1945, 2000, 2015, 2030, 2045, 2100 
                   ]

    times = [
                 '8:00AM', '' , '8:30AM', '' ,  '9:00AM', '' , '9:30AM', '' ,
                '10:00AM', '' , '10:30AM', '' , '11:00AM', '' , '11:30AM', '' ,
                '12:00PM', '' , '12:30PM', '' ,  '1:00PM', '' , '1:30PM', '' ,
                 '2:00PM', '' , '2:30PM', '' ,  '3:00PM', '' , '3:30PM', '' ,
                 '4:00PM', '' , '4:30PM', '' ,  '5:00PM', '' , '5:30PM', '' ,
                 '6:00PM', '' , '6:30PM', '' ,  '7:00PM', '' , '7:30PM', '' ,
                 '8:00PM', '' , '8:30PM', '' ,  '9:00PM'
            ]

    input_files=['my_data.txt']
    title=selected_term

    ## USER DEPENDENT VARIABLES
    f = open("startend.txt", "r")
    line = f.readline()
    items = line.split("/")
    earliest_start = items[0]
    latest_end     = items[1]
    start_index = time_compare_list.index(int(earliest_start))
    end_index = time_compare_list.index(int(latest_end))

    # print(earliest_start)
    # print(latest_end)

    fig=plt.figure(figsize=(10,8))


    ### DO NOT TOUCH THESE ######################################
    # Set Axis
    ax=fig.add_subplot(111)
    ax.yaxis.grid()
    # Set the x-axis on top
    ax.xaxis.tick_top()
    ax.set_xlim(0.5,len(days)+0.5)
    ax.set_xticks(range(1,len(days)+1))
    ax.set_xticks(range(1,len(days)+1), minor=True)
    ax.set_xticklabels(days)
    for tic in ax.xaxis.get_major_ticks():
        tic.tick1On = tic.tick2On = False

    ax.set_ylim(end_index, start_index)
    ax.set_yticks(range(start_index,end_index+1))
    ax.set_yticklabels(times[start_index:])
    ax.set_ylabel('Time')

    # ax.set_ylim(end_index, start_index)
    # ax.set_yticks(range(0,len(times[start_index:end_index])+1))
    # ax.set_yticklabels(times[start_index:])
    # ax.set_ylabel('Time')
    ### DO NOT TOUCH THESE ########################################




    ###### FOR EACH COURSE ITEM ##################################

    f = open("mySchedule.txt", "r")
    lines = f.readlines()
    for line in lines:
        items = line.split("/")
        co_num   = items[0]
        co_id    = items[1]
        co_loc   = items[9]
        co_time_start_AM_or_PM = items[10]
        co_time_end_AM_or_PM = items[11]
        co_time_start_hr  = float(items[4])
        co_time_start_min = float(items[5])
        co_time_end_hr    = float(items[6])
        co_time_end_min   = float(items[7])
        co_time_start_compare = int(items[4] + items[5])
        co_time_start_index   = time_compare_list.index(co_time_start_compare)
        co_time_end_compare = int(items[6] + items[7])

        if co_time_end_min < co_time_start_min:
            co_time_end_hr = co_time_end_hr - 1
            co_time_end_index = co_time_start_index + ((co_time_end_hr - co_time_start_hr) * 4) + ((60 - co_time_start_min) / 15)
        else:
            co_time_end_index = co_time_start_index + ((co_time_end_hr - co_time_start_hr) * 4) + ((co_time_end_min - co_time_start_min) / 15)


        print("items: {}".format(items))

        data     = list(map(float, items[3:-4]))
        co_day   = data[0]
        co_start = data[1] + data[2]/60
        co_end   = co_start + data[5]/60




        # plot event
        plt.fill_between([co_day-0.48, co_day+0.48], [co_time_start_index, co_time_start_index], [co_time_end_index, co_time_end_index], color=colors[int(int(co_num)-1)], edgecolor='k', linewidth=0.5)
        
        # plot event name
        plt.text(co_day, co_time_start_index+1, co_id, ha='center', va='center', fontsize=9, fontweight='bold')

        # plot beginning time
        plt.text(co_day-0.48, co_time_start_index+3, \
            '{0}:{1} {2} - {3}:{4} {5}'.format(items[4], items[5], co_time_start_AM_or_PM, items[6], items[7], co_time_end_AM_or_PM), fontsize=6)
        
        # plot location
        plt.text(co_day+0.48, co_time_start_index+3, co_loc, fontsize=6, horizontalalignment='right')



        print("data: {}".format(data))
        print("co_num: {}".format(co_num))
        print("co_id: {}".format(co_id))
        print("co_day: {}".format(co_day))
        print("co_start: {}".format(co_start))
        print("co_end: {}".format(co_end))
        print("co_loc: {}".format(co_loc))
        print("co_time_start_compare: {}".format(co_time_start_compare))
        print("co_time_start_index: {}".format(co_time_start_index))
        print("co_time_end_compare: {}".format(co_time_end_compare))
        print("co_time_end_index: {}".format(co_time_end_index))
        print("co_time_start_AM_or_PM: {}".format(co_time_start_AM_or_PM))
        print("co_time_end_AM_or_PM: {}".format(co_time_end_AM_or_PM))
        print("\n")


        
    ##################################################################





    plt.title(title,y=1.07)
    plt.savefig('{0}.png'.format(title), dpi=200)


    os.startfile('{0}.png'.format(title))


