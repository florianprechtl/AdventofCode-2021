import os

def readInput(part_path):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, part_path), 'r')
    return f

def readLines(input):
    return [line.strip() for line in input]