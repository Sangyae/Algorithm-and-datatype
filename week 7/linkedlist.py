class Node:
  def __init__(self, init_data):
    self.data = init_data
    self.next = None

  def get_data(self):
    return self.data
  
  def get_next(self):
    return self.next
  
  def set_data(self, new_data):
   self.data = new_data

  def set_next(self, new_next):
   self.next = new_next

def print_chain(n):
   while not n == None:
     print(n.get_data())
     n = n.get_next()
n5 = Node(15)
n6 = Node(34)
n7 = Node(12)
n8 = Node(84)

n6.set_next(n5)
print_chain(n5)
n7.set_next(n8)
n8.set_next(n6)
n5.set_next(None)

print_chain(n5)

print_chain(n6)

print_chain(n7)

print_chain(n8)
