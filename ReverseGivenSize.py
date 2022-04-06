class Node(object):
    def __init__(self,node):
        self.node = node 
        self.next = None 

class Linkedlist:
    def __init__(self):
        self.head = None 

    def insertAtTail(self,new_element):
        new_node = Node(new_element)
        if self.head==None:
            self.head = new_node
            return
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = new_node  
        
    def reverseGivenSize(self,head,k):
        if head is None:
             return None 
        current = head 
        prev = None 
        temp = None 
        count = 0
        while current is not None and count<k:
            temp = current.next 
            current.next = prev 
            prev = current
            current = temp
            count +=1
        if temp:
            head.next = self.reverseGivenSize(temp,k)
        return prev    
    def printlist(self):
        temp = self.head 
        while temp:
            print(temp.node,end=" ")
            temp = temp.next 
                       
                        

A = [1,2,3,4,5,6]
llist = Linkedlist()
for i in A:
    llist.insertAtTail(i)

llist.head=llist.reverseGivenSize(llist.head,3)            
llist.printlist()
