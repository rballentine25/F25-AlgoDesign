"""
Author: Rachael Ballentine
Date: 9/19/25
Description: Doubly linked list implementation
"""

class LinkedList:
    class Node:
        # allow next and prev to be defined with creation to make insert easier
        # default to none for first node creation
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        # when list is created, do not make a first node (list will be empty)
        self.first = None
    
    """ 
    insert method defaults to inserting at the front of the list for simplicity 
    """
    def insert(self, data):
        # if the list is empty, create the first node. Next and prev will still be None
        if self.first is None:
            self.first = self.Node(data)
        # otherwise, create a new node at the front of the list and set it to the first node
        else:
            newNode = self.Node(data, next=self.first)
            self.first.prev = newNode
            self.first = newNode
            
    """ 
    insertAt method allows index to insert at to be defined: inserts BEFORE the node 
    currently at that index. 
    """
    def insertAt(self, data, index=0):
        count = 0
        current = self.first

        # keep track of the number of nodes traversed, and stop when count is one less than index
        # if count is still < index and the next node is null, the index is out of bounds
        while count < index:
            if current.next is None:
                print("ERROR: Index Out of Bounds")
                return
    
            current = current.next
            count += 1
    
        # count < index: new node goes before current node. keep track of current.previous
        # and use it and current to assign new node's next/prev on creation
        previous = current.prev
        newNode = self.Node(data, next=current, prev=previous)

        # change current and previous links
        previous.next = newNode
        current.prev = newNode

    """
    delete method finds the node with the specified data and removes from the list
    by rearranging links between next and previous 
    """
    def delete(self, data):
        # if the list is empty, return
        if self.first is None:
            print("ERROR: List Is Empty")
            return
        
        # if the first node is the one to be deleted, set first to next and change
        # next's links. If self.first is the only node in the list and its data doesn't 
        # match, then the node with the search data doesn't exist
        if self.first.data is data:
            self.first = self.first.next
            self.first.prev = None
            return
        elif self.first.next is None:
            print("ERROR: Node Not Found")
            return
         
        # if node to be deleted was not the first node, traverse the list until the correct node is found
        current = self.first.next
        while current.data is not data:
            # if the current node is not a match and the next one is None, the node with that data does not exist
            if current.next is None:
                print("ERROR: Node Not Found")
                break
            current = current.next

        # at this point, a match has been found: if it is the last node, just change curr.prev
        # if it is not the last node, change both the surrounding nodes
        if current.next is None:
            current.prev.next = None
        else:
            current.next.prev = current.prev
            current.prev.next = current.next
  
    """
    printList traverses the list and prints all node data
    """
    def printList(self):
        if self.first is None:
            print("ERROR: List Is Empty")
            return 
        
        current = self.first
        while(True):
            print(current.data, end=" <-> ")
            if current.next == None:
                print("NONE")
                break
            else:
                current = current.next


# def main():
#     llist = LinkedList()
#     llist.insert(1)
#     llist.insert(2)
#     llist.insert(3)
#     llist.printList()

#     llist.delete(1)
#     llist.printList()

#     llist.insert(5)
#     llist.insertAt(6, index=4)
#     llist.insertAt(6, index=2)
#     llist.printList()

#     llist.delete(5)
#     llist.delete(6)
#     llist.printList()


# main()