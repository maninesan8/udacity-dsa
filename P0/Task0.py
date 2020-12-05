"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    if len(texts) > 0:
        row = texts[0]
        print(f'First record of texts, {row[0]} texts {row[1]} at time {row[2]}')

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    size = len(calls)
    if size > 0:
        row = calls[size - 1]
        print(f'Last record of calls, {row[0]} calls {row[1]} at time {row[2]}, lasting {row[3]} seconds')

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

"""
First record in texts : O(n) => List constructor has to iterate thru all items
Last record in calls : O(n) => List constructor has to iterate thru all items 
"""