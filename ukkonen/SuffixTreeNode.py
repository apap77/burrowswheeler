class SuffixTreeNode:
	def __init__(self, start=None, end=None, suffixLink=None):
		self.children = dict()
		self.start = start
		self.end = end
		self.suffixLink = suffixLink
		self.suffixIndex = -1
		self.leafCount = 0
		self.color = None

	def has_outgoing_edge_starting_with(self, character):
		return character in self.children

	def is_root(self):
		return self.start == -1 and self.end == -1

	def is_leaf(self):
		# return self.suffixIndex != -1
		return len(self.children) == 0

	def get_edge_length(self):
		return self.end - self.start + 1

	def get_child(self, edge):
		return self.children[edge]

	def get_start_position(self):
		return self.start

	def get_end_position(self):
		return self.end

	def set_end_position(self, end):
		self.end = end

	def get_children(self):
		return self.children.values()

	def get_children_lexicographically(self):
		return [value for key, value in sorted(self.children.items(), key=lambda x: x[0])]

	def set_start_position(self, newStart):
		self.start = newStart

	def get_character_index_on_edge(self, edge, distance):
		return self.children[edge].get_start_position() + distance - 1

	def set_suffix_link_to(self, targetNode):
		self.suffixLink = targetNode

	def follow_suffix_link(self):
		return self.suffixLink

	def set_suffix_index(self, suffixIndex):
		self.suffixIndex = suffixIndex

	def get_suffix_index(self):
		return self.suffixIndex

	def set_child(self, edge, node):
		self.children[edge] = node

	def set_new_child(self, edge, start, end):
		child = SuffixTreeNode(start, end)
		self.children[edge] = child

	def set_leaf_count(self, leafCount):
		self.leafCount = leafCount

	def get_leaf_count(self):
		return self.leafCount

	def set_color(self, color):
		self.color = color

	def get_color(self):
		return self.color