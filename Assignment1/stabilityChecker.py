"""
Author: Rachael Ballentine, ballentine.7@wright.edu
Assignment1: Stable Marraige
9/23/25
"""
import StableMatch # import so globals can be used

"""
inputs:
    (StableMatch) sm:     previously initialized StableMatch object, so preference lists etc can be accessed
    (str) toVerifyFile:   file name for the output file to be verified
    (str) fileNum:        number (in string form) to append to the end of the verification file
    (bool) badInput:      flag to specify whether real output from the match algo is being verified, or an
                            intentionally unstable file (for testing of this file)
"""
def stabilityChecker(sm:StableMatch, toVerifyFile, fileNum="", badInput=False):
    file = open(toVerifyFile, 'r')
    matching = []   # matrix to keep track of file contents
    count = 0       # keeps track of the number of lines read, since the last line will be the number of proposals

    # for the first n lines in the file, split the line into the [man, woman] match
    # n+1 line is the num of proposals which we dont care about now 
    for line in file:
        currPair = line.split()
        matching.append([])
        matching[count].append(sm.nameMapMen[currPair[0]])
        matching[count].append(sm.nameMapWomen[currPair[1]])

        count += 1
        if count >=sm.n:
            break
    file.close()

    # if testing an output file that was NOT the result of the matching algorithm, need to update the 
    # womanPartners array to be the same as the matching given in the file. Otherwise, ignore this
    if badInput is True:
        # since matching is in order of men, need a dict to put partners in order of women
        womenMatch = {woman:man for man, woman in matching}
        sm.wPartners = [womenMatch[w] for w in range(sm.n)]

    # actual stability checker algorithm: 
    # outer loop repeats once for each man or until a blocking match is found in the inner loop
    valid = True
    for n in range(sm.n):
        if valid is False:
            break # outer loop: stop reading lines
        
        # set the current man and woman
        currMan = matching[n][0]
        currWife = matching[n][1]

        # for each man, only check the women who he ranked higher than his curr partner
        for w in sm.manPref[currMan]:
            # if the current woman is his current partner, then don't need to keep going through his list
            if w == currWife:
                break # inner loop: go to next man. valid stays true
            
            # else, if one of the man's higher choices prefers him to her current partner, 
            # it is not a stable match
            if sm.ranking[w][currMan] < sm.ranking[w][sm.wPartners[w]]:
                valid = False
                break # blocking pair found, whole matching is unstable
                # else, valid is still true

    # after either every man is checked or a blocking match is found, create verification result file
    outputFile = "Verified" + fileNum + ".txt"
    file = open(outputFile , "w")

    # since the req output is just one line, can use a ternary operator based on the valid bool result
    file.write("stable" if valid else "unstable")
    file.close()
