class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
class Linkedlist:
    def __init__(self):
        self.head = None
    def insertAtHead(self,data):
        node = Node(data)
        node.next = self.head 
        self.head = node 
    def printlist(self):
        temp = self.head 
        while temp:
            print(temp.data,end=" ")
            temp = temp.next 

if __name__=="__main__":
    A = list(map(int,input().split()))
    llist = Linkedlist()
    for i in A:
        llist.insertAtHead(i)
    llist.printlist()                                
