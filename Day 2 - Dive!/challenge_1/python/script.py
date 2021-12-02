import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, '../input.txt'), 'r')

text = f.read()
lines = text.split("\n")

stepsForward = 0
stepsDown = 0

for line in lines:
    if (line != ''):
        m = re.search(r'(\w+)\s(\d+)', line)
        command = m.group(1)
        number = int(m.group(2))

        if (command == "forward"):
            stepsForward += number
        elif (command == "down"):
            stepsDown += number
        elif (command == "up"):
            stepsDown -= number
        else:
            print("error -> should not happen: unknown command")

result = stepsDown * stepsForward

print(result)