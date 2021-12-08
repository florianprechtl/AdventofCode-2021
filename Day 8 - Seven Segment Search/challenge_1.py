from utils import readLines, readInput
import math

def challenge_1():
    input = readInput('input.txt')
    lines = readLines(input)
    lines = [line.split("|")[1] for line in lines]

    result = 0 

    for line in lines:
        output_values = line.split()
        for val in output_values:
            if len(val) in [2, 3, 4, 7]:
                result += 1

    print("Challenge 1 result:", result)
