import re

max_line_length = 158
count = 0
with open('code.js', 'r') as f:
    for line in f:
        while len(line) > max_line_length:
            count=count+1
            split_index = max_line_length
            print(line[:split_index])
            line = line[split_index:]
        print(line)
        print(count)
