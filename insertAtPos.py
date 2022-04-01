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
        
    def insertAtpos(self,pos,data):
        node = Node(data)
        temp = self.head
        i = 0
        while i<pos-1:
            temp = temp.next
            i +=1
        t2 = temp.next
        temp.next = node
        node.next = t2
               
    
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
    llist.insertAtpos(2,20)    
    llist.printlist()   
                                          
