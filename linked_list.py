class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def append(self, data):
    new_node = Node(data)

    if not self.head:
      self.head = new_node
      return

    current = self.head

    while current.next:
      current = current.next

    current.next = new_node

  def prepend(self, data):
      new_node = Node(data)
      # print(new_node.__dict__)
      new_node.next = self.head
      self.head = new_node

  def delete_node(self, key):
    current = self.head
    if current and current.data == key:
      self.head = current.next
      return

    prev = None
    while current and current.data != key:
        prev = current
        current = current.next
    if current:
      prev.next = current.next

  def reverse(self):
    prev = None
    cur = self.head
    while cur:
      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt
    self.head = prev




ll = LinkedList()

ll.append('1frank')
ll.append('2rodrigo')
ll.append('3tony')
ll.print_list()

print('-----')

# # ll.delete_node('')
# ll.print_list()

ll.reverse()
ll.print_list()


