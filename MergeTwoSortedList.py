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

def printlist(head):
    temp = head 
    while temp:
        print(temp.data,end=" ")
        temp = temp.next
    print()
def mergeTwoSortList(head1,head2):
    dummpy = Node(0)
    tail = dummpy
    while head1 and head2:
        if head1.data>head2.data:
            tail.next = head2
            head2 = head2.next
        else:
            tail.next = head1
            head1 = head1.next
        tail= tail.next 
    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2 
    return dummpy.next 
                               
if __name__=="__main__":
    A = list(map(int,input().split()))
    llist1 = Linkedlist()
    for i in A:
        llist1.insertAtTail(i)
    B = list(map(int,input().split()))
    llist2 = Linkedlist()
    for i in B:
        llist2.insertAtTail(i)
    result = mergeTwoSortList(llist1.head,llist2.head)
    printlist(result)
