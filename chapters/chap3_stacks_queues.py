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
		if top == None:
			raise ValueError('No top')
		top = self.top
		self.top = top.next

		return top

	def push(self, value):
		new_node = Node(value)
		new_node.next = self.top
		self.top = new_node

	def peek(self):
		if top == None:
			raise ValueError('No top')
		return self.top

	def is_empty(self):
		return self.top == None

class Queue(object):
	def __init__(self, front=None, back=None):
		self.front = front
		self.back = back

	def add(self, value):
		new_back = Node(value)

		if self.back != None:
			self.back.next = new_back

		if self.front == None:
			self.front = new_back

	def remove(self):
		if self.front == None:
			raise ValueError('No front')

		old_front = self.front
		self.front = self.front.next_node

		if self.front == None:
			self.back = None

		return old_front

	def peek(self):
		if self.back == None:
			raise ValueError('No end')

		return self.back

	def is_empty(self):
		return self.front == None

# 3.1 make this a class?
class ListThreeStacks(object):
	def __init__(self):
		self.full_list = []
		self.stack_starts = [None] * self.num_stacks
		self.stack_ends = [None] * self.num_stacks

	def pop(self, stack_num):
		if self.stack_starts[stack_num] == None:
			raise ValueError('No stack in {}'.format(stack_num))

		element_to_pop = self.full_list[self.stack_starts[stack_num]]
		del self.full_list[self.stack_starts[stack_num]]

		# need to decriment the other stack start / ends
		# i dont think this works
		for i in [number for number > stack_starts in [1,  2 , 3]]:
			try:
				self.stack_starts[stack_num] -= 1
			except:
				self.stack_starts[stack_num] = None

		return element_to_pop

	def push(self, value, stack_num):
		if self.stack_starts[stack_num] == None:


	def peek(self, stack_num):
		if self.stack_starts[stack_num] == None:
			raise ValueError('No start')

		return self.full_list[self.stack_starts[stack_num]]

	def is_empty(self, stack_num):
		return self.stack_starts[stack_num] == None

# 3.2 stack with min in O(1) time
class StackMinTime(Stack):
	def __init__(self, top=None)
		super(StackMinTime,self).__init__()
		self.min_stack = Stack()

	def push(self, value):
		if value <= self.min_stack.peek():
			self.min_stack.push(value)
		super(Stack, self).push()

	def pop(self):
		pop_value = super(Stack, self).pop()
		if pop_value == self.get_min_stack():
			self.min_stack.pop()

		return pop_value

	def get_min_stack():
		if self.min_stack.is_empty():
			return float("inf")
		else:
			return self.min_stack.peek()


# 3.3 stack of plates
class Stack(object):
	def __init__(self, capacity, top=None):
		self.top = None
		self.capacity = capacity
		self.length = 0

	def pop(self):
		if top == None:
			raise ValueError('No top')
		top = self.top
		self.top = top.next
		self.length -= 1

		return top

	def push(self, value):
		new_node = Node(value)
		new_node.next = self.top
		self.top = new_node
		self.length += 1

	def peek(self):
		if top == None:
			raise ValueError('No top')
		return self.top

	def is_empty(self):
		return self.top == None

class StackofStacks(object):
	def __init__(self, capacity):
		self.list_of_stacks = []
		self.capacity

	def pop(self):
		last_stack = _get_last_stack()

		if last_stack == None:
			raise ValueError('No stacks')
		else:
			pop_element = last_stack.pop()

		if last_stack.top == None:
			del last_stack[-1]

		return pop_element

	def push(self, value):
		last_stack = _get_last_stack()

		if last_stack.length == self.capacity or last_stack == None:
			self.list_of_stacks.append(Stack(self.capacity))
			last_stack = _get_last_stack

		last_stack.push(value)

	def _get_last_stack():
		try:
			return self.list_of_stacks[-1]
		except IndexError:
			return None

# 3.4 queue with 2 stacks
# This can be done a lot more simple i think
class MyQueue(object):
	def __init__(self):
		self.main_stack = Stack()
		self.stack_reversed = False

	def _reverse_stack(self):
		temp_stack = Stack()

		if self.is_empty():
			raise ValueError('Stack empty')

		while self.main_stack.pop() != None:
			temp_value = self.main_stack.pop()
			temp_stack.push(temp_value)

		self.main_stack = temp_stack
		self.stack_reversed = not self.stack_reversed

	def add(self, value):
		if self.stack_reversed == True:
			self._reverse_stack()

		self.main_stack.push(value)

	def remove(self, value):
		if self.stack_reversed == False:
			self._reverse_stack()

		self.main_stack.pop()

	def peek(self):
		if self.stack_reversed == False:
			self._reverse_stack()

		return self.main_stack.peek()

	def is_empty(self):
		return self.main_stack.is_empty()

# 3.5 sorted stack
# not quite sure if this is correct
def sort_stack(stack):
	if stack.is_empty():
		raise ValueError('No values')

	sorted_stack = Stack()
	while not stack.is_empty():
		var_to_sort = stack.pop()
		value_sorted = False
		# need to do some kind of condition here
		while value_sorted == False:
			if var_to_sort <= sorted_stack.peek() or sorted_stack.is_empty():
				sorted_stack.push(var_to_sort)
				value_sorted = True
			else:
				higher_value = sorted_stack.pop()
				stack.push(higher_value)

	return sorted_stack

# 3.6
class Animal(object):
	def __init__(self, name, entry_time, animal_type):
		self.name = name
		self.entry_time = entry_time
		self.animal_type = animal_type


class AnimalShelter(object):
	def __init__(self):
		self.dog_queue = Queue()
		self.cat_queue = Queue()

	def enqueue(self, animal):
		if animal.animal_type == 'cat':
			self.cat_queue.add(animal)
		elif animal.animal_type == 'dog':
			self.dog_queue.add(animal)
		else:
			raise ValueError('Bad animal_type')

	def dequeue_any(self):
		try:
			first_cat = self.cat_queue.peek()
		except:
			first_cat = None
			return self.dog_queue.remove()

		try: 
			first_dog = self.dog_queue.peek()
		except:
			first_dog = None
			return self.cat_queue.remove()

		if first_cat == None and first_dog == None:
			raise ValueError('No dogs or cats')

		if first_dog.entry_time >= first_cat.entry_time:
			return self.dog_queue.remove()
		else:
			return self.cat_queue.remove()

	def dequeue_dog(self): 
		if self.dog_queue.is_empty():
			raise ValueError('No dogs')
		else:
			return self.dog_queue.remove()

	def dequeue_cat(self):
		if self.cat_queue.is_empty():
			raise ValueError('No dogs')
		else:
			return self.cat_queue.remove()









