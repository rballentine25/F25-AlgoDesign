import random
from collections import deque
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
    


class Node:
    def __init__(self, mID):
        self.mID = mID
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
    
    def insertFront(self, mID):
        if self.first is None:
            self.first = Node(mID)
        else:
            newNode = Node(mID)
            newNode.next = self.first
            self.first = newNode

    def delete(self, mID):
        if self.first is None:
            return
        
        if self.first.mID == mID:
            self.first = self.first.next
            return
         
        current = self.first
        while current.next is not None:
            if current.next.mID == mID:
                current.next = current.next.next
                break
            current = current.next
            

    def printList(self):
        if self.first is None:
            print("list is empty")
            return 
        
        current = self.first
        while(True):
            print(current.mID)
            if current.next == None:
                break
            else:
                current = current.next

        


#n = None
def main():
    # llist = LinkedList()
    # llist.printList()
    # llist.delete(1)
    # llist.printList()
    # llist.insertFront(1)
    # llist.insertFront(2)
    # llist.insertFront(3)
    # llist.printList()
    # llist.delete(1)
    # print()
    # llist.printList()
    # llist.insertFront(1)
    # llist.delete(3)
    # print()
    # llist.printList()
    # print()
    # llist.insertFront(3)
    # llist.printList()
    # llist.delete(1)
    # print()
    # llist.printList()

    D = deque()
    D.append(5)
    D.append(4)
    D.append(3)
    print(D)
    D.popleft()
    print(D)
    D.popleft()
    print(D)
    D.popleft()
    print(D)
    if len(D) == 0:
        print("empty")

    f = [[None, None] for x in range(3)]
    print(f)

    help = "help"
    help = help + " no"
    print(help)

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