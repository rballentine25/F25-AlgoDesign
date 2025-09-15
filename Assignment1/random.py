import random
import os 

n=5
current = [None]*4
freeMen = [i for i in range(n)]
freeMenRev = [i for i in range(n-1, -1, -1)]
#random.shuffle(freeMen)

print(freeMenRev)
print(freeMen)

print(os.getcwd())
print(os.path.abspath(__file__))

"""
can also do:
inputfile = sys.argv[1] # within the script
on command line:
python filename inputfilepath_forargv1
"""