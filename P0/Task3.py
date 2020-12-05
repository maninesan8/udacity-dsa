"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

area_code_bangalore = '080'
area_codes = set()
bangalore_call_count = 0
total_call_count = 0


def get_area_code(phone_num):
    if phone_num.startswith('('):
        return phone_num[1:phone_num.index(')')]
    elif ' ' in phone_num:
        return phone_num[0:4]
    elif phone_num.startswith('140'):
        return '140'
    return None


def test_get_area_code():
    print(get_area_code('78130 00821'))
    print(get_area_code('(080)45291968'))
    print(get_area_code('(04344)322628'))
    print(get_area_code('1408371942'))
    return


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        caller_area_code = get_area_code(call[0])
        receiver_area_code = get_area_code(call[1])
        if caller_area_code == area_code_bangalore:
            total_call_count += 1
            area_codes.add(receiver_area_code)
            if caller_area_code == receiver_area_code:
                bangalore_call_count += 1

print('The numbers called by people in Bangalore have codes:')
for code in sorted(area_codes):
    print(code)
bangalore_call_percent = bangalore_call_count / total_call_count * 100
print(
    f'{str(round(bangalore_call_percent, 2))} percent of calls from fixed lines in Bangalore are calls to other fixed '
    f'lines in Bangalore.')

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""