import StableMatch

def stabilityChecker(sm:StableMatch, inputFile, toVerifyFile):
    file = open(toVerifyFile, 'r')
    matching = []
    count = 0
    for line in file:
        currPair = line.split()
        matching.append([])
        matching[count].append(sm.nameMapMen[currPair[0]])
        matching[count].append(sm.nameMapWomen[currPair[1]])

        count += 1
        if count >=sm.n:
            break
    file.close()

    valid = True
    for x in range(sm.n):
        if valid is False:
            break # outer loop: stop reading lines

        for w in sm.manPref[matching[x][0]]:
            # if man's current partner is his first choice, it has to be a stable match
            if sm.manPref[matching[x][0] == matching[x][1]]:
                break # inner loop: go to next line. valid stays true
            
            # else, if one of the man's higher choices prefers him to her current partner, 
            # it is not a stable match
            if sm.ranking[w][matching[x][0]] < sm.ranking[w][sm.wPartners[w]]:
                valid = False
                # else, valid is still true

    file = open("Verified.txt" , "w")
    file.write("stable" if valid else "unstable")
    file.close()
