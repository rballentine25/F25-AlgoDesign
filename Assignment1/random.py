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
    llist = LinkedList()
    llist.printList()
    llist.delete(1)
    llist.printList()
    llist.insertFront(1)
    llist.insertFront(2)
    llist.insertFront(3)
    llist.printList()
    llist.delete(1)
    print()
    llist.printList()
    llist.insertFront(1)
    llist.delete(3)
    print()
    llist.printList()
    print()
    llist.insertFront(3)
    llist.printList()
    llist.delete(1)
    print()
    llist.printList()
    #llist.insertFront(1)
    

    # nc = NewClass(5)
    # print(nc.n)

    # num = 3
    # empty = []
    # for i in range(num):
    #     empty.append([0]*num)

    # empty2 = [[0]*num for i in range(num)]

    # print(empty)
    # print(empty2)

    # list1 = [0, 3, 5, 8, 2, 11]
    # list2 = [x for x in list1 if x>3]
    # print(list2)

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