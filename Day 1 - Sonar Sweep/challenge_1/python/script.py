import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Open independetly from the path of the current execution
f = open(os.path.join(__location__, '../input.txt'), 'r')
text = f.read()

# Split by row
lines = text.split("\n")

# Filter for empty line and convert to integer
numbers = [int(line) for line in lines if line != '']

result = 0

# A     -> numbers[i] -> prevNum
#   B   -> numbers[i+1]   -> currNum
for prevNum, currNum in zip(numbers, numbers[1::1]):
    if (currNum > prevNum):
        result += 1

print(result)