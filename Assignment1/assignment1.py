"""
Author: Rachael Ballentine
Assignment 1
"""
import os
dirpath = os.path.dirname(os.path.abspath(__file__))

manPref = []
womanPref = []
ranking = []
current = None
next = None
freeMen = None

def main():
    # validating input file name
    valid = False
    while not valid:
        print("Please enter input file path: ")
        #filename = input() # take input from cmd line
        filename = "Input.txt"
        if os.path.exists(filename):
            print(filename, "valid")
            valid = True
        elif os.path.exists(dirpath + "\\" + filename):
            filename = dirpath + "\\" + filename
            print(filename, "valid")
            valid = True
        else: 
            print("filename invalid")

    if not valid:
        return

    createNameMap(filename)
    

    
def createNameMap(filename):
    allnames = []
    n = None
    file = open(filename, "r")

    n = file.readline().strip() # just read n

    for line in file:
        names = line.split()
        allnames.append(names)
    
    print(n)
    print(allnames)


main()
