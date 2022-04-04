class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
class Linkedlist:
    def __init__(self):
        self.head = None 

    def insertAtTail(self,data):
        node = Node(data)
        if self.head  is None:
            self.head = node 
            return 
        temp = self.head 
        while temp.next!=None:
            temp = temp.next 
        temp.next = node 
        
    def getSize(self):
        n = 0
        temp = self.head
        while temp:
            n +=1
            temp = temp.next 
        return n 
    def delMidElement(self):
        n = self.getSize()
        req = n//2
        i = 1
        temp = self.head
        while i<req:
            temp = temp.next 
            i +=1
        t2 = temp.next 
        temp.next = t2.next 
    
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next 
        print()
        
if __name__=="__main__":
    A = list(map(int,input().split()))
    llist = Linkedlist()
    for i in A:
        llist.insertAtTail(i)
    llist.delMidElement()
    llist.printlist()                       
                      
