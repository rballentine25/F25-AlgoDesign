"""
Author: Rachael Ballentine, ballentine.7@wright.edu
Assignment1: Stable Marraige
9/23/25
"""

from collections import deque # need deque for freeMen 

class StableMatch:
    def __init__(self, filename):
        # establish all global variables
        self.n = None
        self.manPref = []           # men's preferences as read in from input
        self.womanPref = []         # women's preferences as read in from input
        self.ranking = []           # women's prefereces, sorted by the men (index by man gives preference)
        self.proposalCount = 0      # number of proposals
        self.wPartners = []         # each woman's current partner (None to start)
        self.nextW = []             # the next women on a man's pref list that he has not proposed to
        self.freeMen = deque()      # list of free men

        self.nameMapMen = {}        # dictionary for mapping names to numbers for men
        self.nameMapWomen = {}      # dictionary for women: two dicts needed since values repeat
        self.nameMapWomenRev = {}   # used to map numbers for women back to names for output
        self.allNames = []          # matrix for raw input (not divided into men and women)
        self.filename = filename    # input filename
    

        # call the setup function to fill in all the variables
        self.__setup()      
        

    """
    setup method calls the createNameMap and createPrefLists functions to fill in those
    variables, then also fills in the variables that depend on n (read from file). 
    """
    def __setup(self):

        # create name map and preference lists
        self.__createNameMap()
        self.__createPrefLists()

        # after createNameMap reads in n from the input file, the variables that depend
        # on n can be initialized (arrays of size n usually)
        # if the input file was weird or not read right (n is off), just return
        if self.n is not None:
            self.wPartners = [None]*self.n
            self.nextW = [0]*self.n
            
            # put the men in ascending order to start
            for m in range(self.n):
                self.freeMen.append(m)
        else: 
            return

        # print the important arrays to check
        print("Setup Successful!")
        print("\tMen Preferences:", self.manPref)
        print("\tWomen Preferences:", self.womanPref)
        print("\tWomen's Rankings:", self.ranking)
        print("\tFree Men Linked List:", self.freeMen)


    """
    createNameMap opens the input file and finds n and all the names. 
    after all the names are read in, the method creates dictionaries to map the 
    names to numbers based on the order they appear in the input file (does not
    rely on whether they are alphabetical, ex "Briana Amy Chelsea" will map as 
    Briana-0 Amy-1 Chelsea-2 rather than Amy-0 Briana-1 Chelsea-2). 
    """
    def __createNameMap(self):
        # open the input file and read
        file = open(self.filename, "r")

        # read first line, strip the whitespace chars, and cast to an integer
        self.n = int(file.readline().strip()) # just read n

        # for each line in the file, split by whitespace into an array and append 
        # those names to the names matrix
        for line in file:
            names = line.split()
            self.allNames.append(names)

        # assuming input file has names in alphabetical order
        row = 0
        # assign numbers to the men: rows 0:n
        for i in range(self.n): 
            self.nameMapMen[self.allNames[row][0]] = i 
            row += 1

        # assign numbers to the women: rows n+1:2n
        for j in range(self.n):
            self.nameMapWomen[self.allNames[row][0]] = j
            row += 1

        # create reversed map for women so creating output file is easier later
        self.nameMapWomenRev = {name:num for num,name in self.nameMapWomen.items()}
        file.close()

    """
    createPrefLists uses the name maps just created in previous method to create the numerical
    preference lists for the men and women. also calls createRanking at the end, only after the 
    women's pref list has been created    
    """
    def __createPrefLists(self):
        # create the men's preference lists
        for m in range(self.n):
            self.manPref.append([])
            for w in range(1, self.n+1):
                # in the current row (man), match the next woman from the input file to her
                # id in the name map and append that id to the man pref matrix
                self.manPref[m].append(self.nameMapWomen[self.allNames[m][w]])

        # create the women's preference lists
        # since allNames has to be indexed between n:2n-1 (0 based) to get correct row, 
        # need another var to keep track of current row in womanPref
        prefRow = 0
        for w in range(self.n, 2*self.n): # second half of the input matrix
            self.womanPref.append([])
            for m in range(1, self.n+1):
                # for each women, match each man in her list to his id and add to pref list
                self.womanPref[prefRow].append(self.nameMapMen[self.allNames[w][m]])
            prefRow += 1

        # once the preference lists have been created, call createRanking to make the women's ranking list
        self.__createRanking()

    """
    createRanking traverses the women's preference list and inverts it to get the ranking per man 
    """
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