class Node(object):
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node

	def set_next(self, new_next):
		self.next_node = new_next

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next_node


class LinkedList(object):
	def __init__(self, head=None)
		self.head = head

	def insert_node(self, value):
		new_node = Node(value)
		new_node.set_next(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()

		return count

	def search(self, value):
		found = False
		current = self.head

		while found = False and current:
			if current.get_value() == value:
				found = True
			else:
				current = current.get_next()

		if current == None:
			raise ValueError('could not find value')

		return current

	def print_list(self):
		current = self.head
		list_str = ''

		while current:
			list_str = list_str + current.value
			if current.next_node != None:
				list_str = list_str + ' -> '

		return list_str

# 2.1
	def remove_duplicates(self):
		current = self.head
		previous = None
		value_counter = {}

		while current:
			if value_counter[current.get_value()] > 0:
				previous.set_next(current.get_next())
			else:
				value_counter[current.get_value()] += 1
				previous = current
		
			current = current.get_next()

		if current == None:
			raise ValueError('couldnt find value')

# 2.1 no temp buffer
	def remove_duplicates_no_buff(self):
		current = self.head

		while current != None:
			runner = current
			while runner.next_node != None:
				if runner.next_node.get_value() == current.get_value():
					runner.next_node = runner.next_node.next_node
				else:
					runner = runner.get_next()

			current = current.get_next()

		if current == None:
			raise ValueError('couldnt find value')

# 2.2
	def kth_to_last(self, k):
		kth_pointer = self.head
		k_spacer = self.head

		for i in range(k):
			if k_spacer is None:
				return None
			else:
				k_spacer = k_spacer.get_next()

		while k_spacer is not None:
			k_spacer = k_spacer.get_next()
			kth_pointer = kth_pointer.get_next()

		return kth_pointer.get_value()

# 2.3
	@staticmethod
	def delete_middle_node(node):
		if node == None or node.next_node == None:
			return False

		next_node = node.next_node
		node.value = next_node.value
		node.next_node = next_node.next_node
		# does this delete the node?
		node.next_node = node.next_node.next_node

		return True

# 2.4
	def partition_list(self, partition_num):
		current = self.head
		perm_head = self.head

		while current:
			if current.value < partition_num:
				# do the upsert here
				node_begin = current
				node_begin.next_node = perm_head
				perm_head = new_node
				# delete old node
				current.next_node = current.next_node.next_node

			current = current.get_next()

		return self.print_list()

# 2.5 digits reverse order
	def add_digits_reverse(self, list_one, list_two, add_tens):
		if list_one == None and list_two == None and add_tens == 0:
			return None

		added_node = Node()

		l1_value = list_one.value if list_one != None else 0
		l2_value = list_two.value if list_two != None else 0	

		node_sum = (add_tens + l1_value + l2_value)
		node_value = node_sum % 10
		add_tens = 1 if node_sum >= 10 else 0

		added_node.value = node_value

		if list_one != None or list_two != None:
			result = add_digits_reverse(list_one.get_next(), list_two.get_next(), add_tens)

		added_node.next_node = result

		return added_node

	def add_digits_reverse(self, list_one, list_two):
		l1_current = list_one.head
		l2_current = list_two.head
		l1_num_str = ''
		l2_num_str = ''

		while l1_current != None:
			# maybe have a value check for numbs > 9?
			l1_num_str = l1_num_str + str(l1_current.value)
			l1_current = l1_current.get_next()

		while l2_current != None:
			# maybe have a value check for numbs > 9?
			l2_num_str = l2_num_str + str(l2_current.value)
			l2_current = l2_current.get_next()
		
		return int(l1_num_str) + int(l2_num_str)

# 2.5 standard order

	def add_digits_standard(self, list_one, list_two):
		l1_current = list_one.head
		l2_current = list_two.head
		l1_num_str = ''
		l2_num_str = ''

		while l1_current != None:
			# maybe have a value check for numbs > 9?
			l1_num_str = l1_num_str + str(l1_current.value)
			l1_current = l1_current.get_next()

		while l2_current != None:
			# maybe have a value check for numbs > 9?
			l2_num_str = l2_num_str + str(l2_current.value)
			l2_current = l2_current.get_next()

		l1_num_str.reverse
		l2_num_str.reverse
		
		return int(l1_num_str) + int(l2_num_str)

# 2.6 palindrone
	def reverse(self, node):
		previous = None
		current = node

		while current != None:
			next_n = current.get_next()
			current.next_node = previous
			previous = current
			current = next_n

		return previous 

	def is_palindrone(self):
		current = self.head
		reversed_list = reverse(current)

		while reversed_list != None and current != None:
			if reversed_list.get_value() != current.get_value():
				return False

			reversed_list = reversed_list.get_next()
			current = current.get_next()

		return reversed_list == None and current == None

# 2.7
	@staticmethod
	def is_intersecting(head1, head2):
		one = head1
		two = head2

		one_counter = 0
		two_counter = 0

		if one == two:
			return True

		while one != None:
			one_counter += 1
			one = one.get_next()

		while two != None:
			two_counter += 1
			two = two.get_next()

		if one != two:
			return False

		#fast forward one of them
		difference = abs(one_counter - two_counter)
		one_final = head1
		two_final = head2

		if one_counter > two_counter:
			for i in range(difference):
				one_final = one_final.get_next()	
		elif two_counter < one_counter:
			for i in range(difference):
				two_final = two_final.get_next()

		# find the actual intersection
		while one_final != None and two_final != None:
			if one_final == two_final: 
				return one_final

			one = one.get_next()
			two = two.get_next()

		return False

# 2.8
	def is_loop(self)
		current = self.head
		runner = self.head.get_next()

		if self.head() == None:
			raise ('Head doesnt exist')

		while current != None:
			if current == runner:
				return runner

			current = current.get_next()
			runner = runner.get_next().get_next()

		return False

