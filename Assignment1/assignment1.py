"""
Author: Rachael Ballentine, ballentine.7@wright.edu
Assignment1: Stable Marraige
9/23/25
"""
# import all needed modules
import os, sys
import stabilityChecker as scheck
import StableMatch as SM

# find the path of the current folder to use for file names later
dirpath = os.path.dirname(os.path.abspath(__file__))

def main():
##### VALIDATING INPUT FILE NAME FROM CMD LINE ARG ####
    inputArg = sys.argv[1] 

    # If the input file name had a number, find the number based on expected name pattern
    # will be used for naming output and verification files later
    expected = "Input"
    start = inputArg.find(expected) + len(expected)
    end = inputArg.find(".txt")
    fileNum = inputArg[start:end] 

    # verify that the input file specified actually does exist before opening it
    if os.path.exists(inputArg):
        filename = inputArg
    elif os.path.exists(dirpath + "\\" + inputArg):
        filename = dirpath + "\\" + inputArg
    else: 
        print("Filename invalid")
        return

    # create a stable match object by passing the input file name
    # stable match class parses the file and creates all preference lists and rankings
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
    # now that the stable match class has prepared all the needed variables, actaully find the matches
    # keep track of the matches in a new matrix
    matches = [[x, None] for x in range(sm.n)]

    # while there is still a free man:
    while len(sm.freeMen) != 0: 
        currM = sm.freeMen.popleft() # pop the next free man off the deque
        wID = sm.nextW[currM] # for the currM, find the next woman he has not proposed to in his pref list
        currW = sm.manPref[currM][wID] 
        
        # if that woman is not currently engaged, then she is now engaged to the current man
        # set her partner to currM in the partners list and update the matches matrix
        if sm.wPartners[currW] is None:
            sm.wPartners[currW] = currM
            matches[currM][1] = currW
        # if that woman is engaged, but likes currM more than her current partner, then she is now
        # engaged to currM. Put her previous partner back in the free men deque, then update the partners
        # list and the matches matrix
        elif sm.ranking[currW][currM] < sm.ranking[currW][sm.wPartners[currW]]:
            sm.freeMen.appendleft(sm.wPartners[currW])
            matches[sm.wPartners[currW]][1] = None
            sm.wPartners[currW] = currM
            matches[currM][1] = currW
        # if that woman is engaged but likes her current partner more than currM, put currM back in the 
        # free men deque (in the back) and continue on to the next man
        else:
            sm.freeMen.appendleft(currM)

        # for each loop, increment the total number of proposals and the number of proposals for the currM
        sm.proposalCount += 1
        sm.nextW[currM] += 1

    print("Matching complete:", matches)


#### PRINTING TO OUTPUT FILE ####
    # matches were made still in numerical form, so now convert back to characters to print to output file
    outputTxt = [[None, None] for x in range(sm.n)]
    for x in range(sm.n):
        # print men in original order of all names. use the reversed name map for the women to match them 
        # in whatever order they appear in the matches list (stable match class also prepped this reverse name map)
        outputTxt[x][0] = sm.allNames[x][0]
        outputTxt[x][1] = sm.nameMapWomenRev[matches[x][1]]

    # convert from matrix of names to a string to print to the file (concatenate for each line in the matrix)
    string = ""
    for x in range(sm.n):
        string = string + outputTxt[x][0] + " " + outputTxt[x][1] + "\n"

    # finally, create the output file and print the string to it. 
    # if only one cmd line arg was given, open an output file (using the filenum found earlier) and print the 
    # concatenated string to it as well as proposal count, then run stability checker on that output file
    if len(sys.argv) == 2:
        outputName = "Output"
        outputName = (outputName + fileNum + ".txt") if len(fileNum) != 0 else (outputName + ".txt")
        file = open(outputName, 'w')
        file.write(string)
        file.write(str(sm.proposalCount))
        file.close()
        scheck.stabilityChecker(sm, outputName, fileNum)
    # extra arg used to verify false output is unstable (for stability checker tests). if the extra 
    # arg was provided, that means the stability checker should be run on that "fake" output file not the 
    # one just generated. don't bother creating a new output file, just run the stability checker on providide input
    elif len(sys.argv) > 2:
        verifyFile = sys.argv[2]
        print("Verifying:", verifyFile)
        scheck.stabilityChecker(sm, toVerifyFile=verifyFile, fileNum=fileNum, badInput=True)
    else:
        print("freak out! idk man")

# call main
main()
