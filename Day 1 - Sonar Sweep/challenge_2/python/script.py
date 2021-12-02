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

# numbers[i-1] + numbers[i-2] can be ommited
# A     -> numbers[i] -> currReducedSum
# A B   -> numbers[i+1] + numbers[i-2]
# A B   -> numbers[i+1] + numbers[i-2]
#   B   -> numbers[i+3] -> prevReducedSum
for prevReducedSum, currReducedSum in zip(numbers, numbers[3::1]):
    if (currReducedSum > prevReducedSum):
        result += 1

print(result)