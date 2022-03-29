class Node:
	def __init__(self,data):
		self.data = data 
		self.next=None 

class Linkedlist:
	def __init__(self):
		self.head = None 

	def insertAtTail(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return 
		temp = self.head
		while temp.next!=None:
			temp = temp.next 
		temp.next = new_node

	def insertAtHead(self,data):
		new_node = Node(data)

		new_node.next = self.head
		self.head = new_node

	def printlist(self):
		temp = self.head
		while temp:
			print(temp.data,end=" ")
			temp = temp.next 

llist = Linkedlist()
A = list(map(int,input().split()))
for i in A:
	llist.insertAtTail(i)

llist.printlist()