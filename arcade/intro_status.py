import os
import re

# Define the directory path
directory = r'C:\Users\Public\Dev\practice\python-exercises\code-signal\arcade\1. Intro (60)'

# Initialize counters for different types of files
not_explored_count = 0
consulted_count = 0
not_solved_count = 0
solved_count = 0
leave_for_next_count = 0

# Define the regex pattern to match file names
pattern = r'^\d+\.\s*-\s*([+]+|-)\s*\.py$'

# Traverse the directory and its subfolders
for root, _, files in os.walk(directory):
    for filename in files:
        # Check if the file name matches the pattern
        if re.match(pattern, filename):
            match = re.match(pattern, filename)
            type_indicator = match.group(1)
            
            if type_indicator == '-':
                not_explored_count += 1
            elif type_indicator == '-+++':
                consulted_count += 1
            elif type_indicator == '-+-':
                not_solved_count += 1
            elif type_indicator == '--':
                solved_count += 1
            elif type_indicator == '-++':
                leave_for_next_count += 1

# Print the counts for each type of file
print(f'Not Explored: {not_explored_count}')
print(f'Consulted: {consulted_count}')
print(f'Not Solved: {not_solved_count}')
print(f'Solved: {solved_count}')
print(f'Leave for Next: {leave_for_next_count}')
