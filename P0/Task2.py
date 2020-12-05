"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

### dictionary of phone number to the time spent. also keep track of max time for current number after adding
max_duration = 0
max_number = None
number_duration = {}


def set_max_details(phone_num_1, phone_num_2, duration):
    duration = int(duration)
    global max_duration
    global max_number
    number_duration[phone_num_1] = number_duration.get(phone_num_1, 0) + duration
    number_duration[phone_num_2] = number_duration.get(phone_num_2, 0) + duration
    if number_duration[phone_num_1] > number_duration[phone_num_2] and number_duration[phone_num_1] > max_duration:
        max_duration = number_duration[phone_num_1]
        max_number = phone_num_1
    elif number_duration[phone_num_2] > max_duration:
        max_duration = number_duration[phone_num_2]
        max_number = phone_num_2


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        ### row[0] and row[1] both spend time
        set_max_details(row[0], row[1], row[3])

print(f'{max_number} spent the longest time, {max_duration} seconds, on the phone during September 2016')

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""