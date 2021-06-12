# Implementation of linked list in python
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def printList(self):
        if self.head is None:
            return "No node to print"
        printList = self.head
        while printList is not None:
            print(printList.val)
            printList = printList.next
        return "End"
        
    def insertBeginning(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def insertEnd(self, node):
        if self.head is None:
            self.head = node
        else:
            prevNode = self.head
            while prevNode.next is not None:
                prevNode = prevNode.next
            prevNode.next = node
            
    def delete(self, key):
        if self.head is None:
            return 'No node to delete'
        
        if self.head.val == key:
            self.head = self.head.next
            return 'Removed Head Node'
            
        loopList = self.head.next 
        prev = self.head
        while loopList is not None:
            if loopList.val == key:
                prev.next = loopList.next
                return 'Removed key', key
                
            prev = loopList    
            loopList = loopList.next
        return 'Could not find key in the linkedList'
                
            
    
myList = LinkedList()
firstNode = Node(1)
myList.head = firstNode
myList.insertBeginning(Node(0))
myList.insertEnd(Node(2))
myList.insertEnd(Node(3))
myList.insertEnd(Node(4))
myList.insertEnd(Node(5))
print(myList.delete(0))
print(myList.printList())
