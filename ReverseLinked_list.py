class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
class Linkedlist:
    def __init__(self):
        self.head = None 
    def insertAtTail(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node 
            return 
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = node 
        
    def reverseList(self):
        if self.head.next is None:
            return 
        prev = None
        cur = self.head 
        while cur:
            t2 = cur.next 
            cur.next = prev
            prev = cur 
            cur = t2 
        self.head = prev         
    
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next 

if __name__=="__main__":
    A = list(map(int,input().split()))
    llist = Linkedlist()
    for i in A:
        llist.insertAtTail(i)
    llist.reverseList()    
    llist.printlist()   
                                          
