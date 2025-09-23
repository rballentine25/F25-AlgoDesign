"""
Author: Rachael Ballentine
Assignment 1
"""
import os
import stabilityChecker as scheck
import StableMatch as SM

dirpath = os.path.dirname(os.path.abspath(__file__))

def main():
##### VALIDATING INPUT FILE NAME ####
    valid = False
    while not valid:
        print("Please enter input file path: ")
        filename = input() # take input from cmd line
        #filename = "Input.txt"
        if os.path.exists(filename):
            print(filename, "valid")
            valid = True
        elif os.path.exists(dirpath + "\\" + filename):
            filename = dirpath + "\\" + filename
            print(filename, "valid")
            valid = True
        else: 
            print("filename invalid")

    sm = SM.StableMatch(filename)


#### MATCHING ALGORITHM ####
    
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

    matches = [[x, None] for x in range(sm.n)]
    while len(sm.freeMen) != 0:
        currM = sm.freeMen.popleft()
        wID = sm.nextW[currM]
        currW = sm.manPref[currM][wID]
        
        if sm.wPartners[currW] is None:
            sm.wPartners[currW] = currM
            matches[currM][1] = currW
        elif sm.ranking[currW][currM] < sm.ranking[currW][sm.wPartners[currW]]:
            sm.freeMen.appendleft(sm.wPartners[currW])
            matches[sm.wPartners[currW]][1] = None
            sm.wPartners[currW] = currM
            matches[currM][1] = currW
        else:
            sm.freeMen.appendleft(currM)

        sm.proposalCount += 1
        sm.nextW[currM] += 1

    print("Matching complete:", matches)


#### PRINTING TO OUTPUT FILE ####
    outputTxt = [[None, None] for x in range(sm.n)]
    for x in range(sm.n):
        outputTxt[x][0] = sm.allNames[x][0]
        outputTxt[x][1] = sm.nameMapWomenRev[matches[x][1]]

    print(outputTxt)
    print(sm.proposalCount)

    string = ""
    for x in range(sm.n):
        string = string + outputTxt[x][0] + " " + outputTxt[x][1] + "\n"


    outputName = input("Name of output file: ")
    file = open(outputName, 'w')
    file.write(string)
    file.write(str(sm.proposalCount))
    file.close()

    scheck.stabilityChecker(sm, inputFile=filename, toVerifyFile=outputName)

main()
