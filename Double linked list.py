class node:
  def __init__ (self,data):
    self.data=data
    self.next=None
    self.prev=None
 
class dll:
  def __init__ (self):
    self.head=None
    
  def display(self):
    if self.head is None:
      print("Empty list")
    else:
      self.head=temp
      while temp:
        print(temp.data, "-->" , end=' ')
        temp=temp.next

L=dll()
  n1=node(Amandeep Singh,39)
  self.head=n1
   n2=node(KIRANJEET KAUR,38)
    n1.next=n2
n2.prev=n1
n3=node(Tanveer Singh,19)
n2.next=n3
n3.prev=n2
n4=node(Khushpreet Kaur,16)
n4.prev=n3
n3.next=n4
L.display()
 
