class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_bingo_field(bingoField, calledNumbers):
    for y in range(len(bingoField)):
        for x in range(len(bingoField[0])):
            if (bingoField[y][x] in calledNumbers):
                print(f"{bcolors.WARNING}{str(bingoField[y][x]).ljust(2)}{bcolors.ENDC}", end='')
            else:
                print(str(bingoField[y][x]).ljust(2), end='')
            
            if (x != (len(bingoField[0]) - 1)):
                print(" ", end='')
        print("") 
    print("")