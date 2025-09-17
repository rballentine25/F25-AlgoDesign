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

class NewClass:
    def __init__(self, number):
        self.n = number
    


#n = None
def main():
    nc = NewClass(5)
    print(nc.n)

    num = 3
    empty = []
    for i in range(num):
        empty.append([0]*num)

    empty2 = [[0]*num for i in range(num)]

    print(empty)
    print(empty2)

    list1 = [0, 3, 5, 8, 2, 11]
    list2 = [x for x in list1 if x>3]
    print(list2)

def method1(n):
    n = 4

def method2(n):
    print(n)
    n = 6

main()
"""
can also do:
inputfile = sys.argv[1] # within the script
on command line:
python filename inputfilepath_forargv1
"""