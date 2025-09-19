"""
Author: Rachael Ballentine
Assignment 1
"""
import os
from LinkedList import * # my script for a doubly linked list

dirpath = os.path.dirname(os.path.abspath(__file__))

class StableMatch:
    def __init__(self):
        # establish all global variables
        self.n = None
        self.manPref = []      # men's preferences as read in from input
        self.womanPref = []    # women's preferences as read in from input
        self.ranking = []      # women's prefereces, sorted by the men (index by man gives preference)
        self.proposalCount = 0 # number of proposals
        self.wPartners = []    # each woman's current partner (None to start)
        self.nextW = []        # the next women on a man's pref list that he has not proposed to
        self.freeMen = LinkedList() # list of free men (unengaged)

        self.nameMap = {}
        self.allNames = []

        self.filename = ""

        
    def setup(self, filename):
        self.filename = filename

        # create name map
        self.__createNameMap()
        self.__createPrefLists()

        if self.n is not None:
            self.wPartners = [None]*self.n
            self.nextW = [0]*self.n
            
            for m in range(self.n):
                self.freeMen.insertBack(m)
        else: 
            return

        print("Setup Successful!")
        print("\tAll Names:", self.allNames)
        print("\tMen Preferences:", self.manPref)
        print("\tWomen Preferences:", self.womanPref)
        print("\tWomen's Rankings:", self.ranking)
        print("\tFree Men Linked List:", self.freeMen.printString())


    """
    Initially all m in the set M and all w in the set W are free
    While there is a man m who is free and hasn't proposed to every woman
        Choose such a man m
        Let w be the highest ranked woman in m's preference list to whom m
            has not yet proposed
        If w is free then 
            (w, m) become engaged
        Else w is currently engaged to m'
            If w prefers m' to m then
                m remains free
            Else w prefers m to m'
                (m, w) become engaged
                m' becomes free
            Endif
        Endif
    Endwhile
    Return the set S of engaged pairs
    """
    def performMatching(self):
        # this is very much not working will prob have to completely rewrite
        while self.freeMen.isEmpty() is not True:
            currM = self.freeMen.first.data
            currW = self.nextW[currM]
            wCurrPartner = self.wPartners[currW]
            print("currM =", currM, "\ncurrW =", currW)

            # the next woman is not engaged
            if wCurrPartner is None:
                self.wPartners[currW] = currM
                self.freeMen.delete(currM)
                print("currW not engaged, (", currM, ",", currW, ") now engaged")
            # the next woman IS engaged, but prefers m to m'
            elif self.ranking[currW][currM] > self.ranking[currW][wCurrPartner]:
                self.freeMen.insertBack(wCurrPartner)
                self.wPartners[currW] = currM
                self.freeMen.delete(currM)
                print("currW preferred", currM, "to", wCurrPartner, "(", currM, ",", currW, "now engaged")
            # the next woman IS engaged, AND prefers m' to m
            else:
                # m is rejected by w. Move him to the back of the list?
                self.freeMen.delete(currM)
                self.freeMen.insertBack(currM)
                print("currW,", currW, "rejected currM,", currM)
                
            self.proposalCount += 1
            self.nextW[currM] += 1

        


    def __createNameMap(self):
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


    def __createPrefLists(self):
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

        # once the preference lists have been created, call createRanking to make the women's ranking list
        self.__createRanking()
        

    def __createRanking(self):
        # create an nxn empty matrix for womens rankings
        self.ranking = [[0]*self.n for x in range(self.n)]

        # fill in the ranking linearly with a single pass through women's pref list (n^2)
        # for each man in the women's pref list, remember his id and use that to index into
        # the ranking list. insert the current val i for his pref ranking in the ranking list
        for w in range(self.n):
            for i in range(self.n):
                rank = self.womanPref[w][i]
                self.ranking[w][rank] = i

    

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

    sm = StableMatch()
    sm.setup(filename)
    print()
    sm.performMatching()



main()
