class Node(object):
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node

	def set_value(self, value):
		self.value = value

class Stack(object):
	def __init__(self, top=None):
		self.top = None

	def pop(self):
		top = self.top
		self.top = top.next

		return top

	def push(self, value):
		new_node = Node(value)
		new_node.next = self.top
		self.top = new_node

	def peek(self):
		return self.top

	def is_empty(self):
		return self.top == None
			