import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, '../input.txt'), 'r')

text = f.read()
lines = text.split("\n")

depth = 0
horz = 0
aim = 0

for line in lines:
    if (line != ''):
        m = re.search(r'(\w+)\s(\d+)', line)
        command = m.group(1)
        number = int(m.group(2))

        if (command == "forward"):
            horz += number
            depth += aim * number
        elif (command == "down"):
            aim += number
        elif (command == "up"):
            aim -= number
        else:
            print("error -> should not happen: unknown command")

result = depth * horz

print(result)
