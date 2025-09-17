"""
Author: Rachael Ballentine
Assignment 1
"""
import os
dirpath = os.path.dirname(os.path.abspath(__file__))

class StableMatchSetup:
    def __init__(self, filename):
        # establish all global variables
        self.n = None
        self.manPref = []
        self.womanPref = []
        self.ranking = []

        self.nameMap = {}
        self.allNames = []
        self.filename = filename

        # create name map
        self.createNameMap()
        self.createPrefLists()

        if self.n is not None:
            self.current = [None]*self.n
            self.next = [0]*self.n
            self.freeMen = [i for i in range(self.n)]


    def createNameMap(self):
        file = open(self.filename, "r")

        self.n = int(file.readline().strip()) # just read n

        for line in file:
            names = line.split()
            self.allNames.append(names)

        # assuming input file has names in alphabetical order
        row = 0
        # assign numbers to the men: rows 0:n
        for i in range(self.n): 
            self.nameMap[self.allNames[row][0]] = i 
            row += 1

        # assign numbers to the women: rows n+1:2n
        for j in range(self.n):
            self.nameMap[self.allNames[row][0]] = j
            row += 1


    def createPrefLists(self):
        # create the men's preference lists
        for m in range(self.n):
            self.manPref.append([])
            for w in range(1, self.n+1):
                # in the current row (man), match the next woman from the input file to her
                # id in the name map and append that id to the man pref matrix
                self.manPref[m].append(self.nameMap[self.allNames[m][w]])

        # create the women's preference lists
        # since allNames has to be indexed between n:2n-1 (0 based) to get correct row, 
        # need another var to keep track of current row in womanPref
        prefRow = 0
        for w in range(self.n, 2*self.n): # second half of the input matrix
            self.womanPref.append([])
            for m in range(1, self.n+1):
                # for each women, match each man in her list to his id and add to pref list
                self.womanPref[prefRow].append(self.nameMap[self.allNames[w][m]])
            prefRow += 1

        print("manPref list: ", self.manPref)
        print("womanPref list: ", self.womanPref)

        # once the preference lists have been created, call createRanking to make the women's ranking list
        self.createRanking()
        

    def createRanking(self):
        # create an nxn empty matrix for womens rankings
        self.ranking = [[0]*self.n for x in range(self.n)]

        # fill in the ranking linearly with a single pass through women's pref list (n^2)
        # for each man in the women's pref list, remember his id and use that to index into
        # the ranking list. insert the current val i for his pref ranking in the ranking list
        for w in range(self.n):
            for i in range(self.n):
                rank = self.womanPref[w][i]
                self.ranking[w][rank] = i
        
        print("ranking: ", self.ranking)
        



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

    sm = StableMatchSetup(filename)

    print(sm.allNames, "\n", sm.nameMap)
    print("\n")

    #createPrefLists()
    #print(globals.manPref)




main()
