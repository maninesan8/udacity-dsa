"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


text_numbers = set()
call_receivers = set()
tele_marketers = set()


def is_telemarketer(phone_number):
    return phone_number not in text_numbers and phone_number not in call_receivers


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        text_numbers.add(text[0])
        text_numbers.add(text[1])


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        call_receivers.add(call[1])
    for call in calls:
        if is_telemarketer(call[0]):
            tele_marketers.add(call[0])

print('These numbers could be telemarketers: ')
for tele_marketer in sorted(tele_marketers):
    print(tele_marketer)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""