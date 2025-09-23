from collections import deque

class StableMatch:
    def __init__(self, filename):
        # establish all global variables
        self.n = None
        self.manPref = []      # men's preferences as read in from input
        self.womanPref = []    # women's preferences as read in from input
        self.ranking = []      # women's prefereces, sorted by the men (index by man gives preference)
        self.proposalCount = 0 # number of proposals
        self.wPartners = []    # each woman's current partner (None to start)
        self.nextW = []        # the next women on a man's pref list that he has not proposed to
        self.freeMen = deque() # list of free men

        self.nameMapMen = {}
        self.nameMapWomen = {}
        self.nameMapWomenRev = {}
        self.allNames = []
        self.filename = filename
    
        self.__setup(filename)
        

    def __setup(self, filename):
        self.filename = filename

        # create name map
        self.__createNameMap()
        self.__createPrefLists()

        if self.n is not None:
            self.wPartners = [None]*self.n
            self.nextW = [0]*self.n
            
            for m in range(self.n):
                #self.freeMen.insertBack(m)
                self.freeMen.append(m)
        else: 
            return

        print("Setup Successful!")
        print("\tAll Names:", self.allNames)
        print("\tMen Preferences:", self.manPref)
        print("\tWomen Preferences:", self.womanPref)
        print("\tWomen's Rankings:", self.ranking)
        print("\tFree Men Linked List:", self.freeMen)
        print("\tName map:", self.nameMapMen, self.nameMapWomen)


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
            self.nameMapMen[self.allNames[row][0]] = i 
            row += 1

        # assign numbers to the women: rows n+1:2n
        for j in range(self.n):
            self.nameMapWomen[self.allNames[row][0]] = j
            row += 1

        self.nameMapWomenRev = {name:num for num,name in self.nameMapWomen.items()}
        file.close()


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