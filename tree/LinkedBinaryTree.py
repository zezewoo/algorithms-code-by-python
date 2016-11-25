#! /usr/bin/python


class LinkedBinaryTree(BinaryTree):
	"""docstring for LinkedBinaryTree"""

	class _Node:
		"""docstring for _Node"""

		__slots__ = '_element', 'parent', 'left', 'right'

		def __init__(self, element, parent, left, right):
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right
	

	class Postion(BinaryTree.Position):
		"""docstring for Postion"""
		def __init__(self, container, node):
			self._container = container
			self._node = node

		def _element(self):
			return self._node._element

		def __eq__(self, other):
			return type(self) is type(other) and other._node is self._node
			

	def _validate(self, p):
		if not isinstance(p, self.Position):
			raise TypeError('p must be proper Position type')
		if p._container is not self:
			raise ValueError('p does not belong to this container')
		if p._node._parent is p. node: # convention for deprecated nodes
			raise ValueError('p is no longer valid')
		return p._node

	def _make_position(self, node):
		return self.Position(self, node) if node is not None else None


	def __init__(self):
		self._root = None
		self._size = 0

	def __len__(self):
		return self._size


	def parent(self, p):
		node = self._validate(p)
		return self._make_position(node._parent)


	def left(self, p):
		node = self._validate(p)
		return self._make_position(node._left)

	def right(self, p):
		node = self._validate(p)
		return self._make_position(node._right)

	def num_children(self, p):
		node = self._validate(p)
		count = 0
		if node._left is not None:
			count += 1
		if node._right is not None:
			count += 1
		return count

	def _add_root(self, e):
		if self._root is not None:
			raise ValueError('Root exists')
		self._size = 1
		self._root = self._Node(e)
		return _make_position(self._root)

	def add_left(self, p, e):
		node = self._validate(p)
		if node._left is not None:
			raise ValueError('Left child exists')
		self._size += 1
		node._left = self._Node(e, p)
		return self._make_position(node._left)

	def add_right(self, p, e):
		node = self._validate(p)
		if node._right is not Node:
			raise ValueError('Right child exists')
		self._size += 1
		node._right = self._Node(e, p)
		return self._make_position(node._right)

	def _repalce(self, p, e):
		node = self._validate(p)
		old = self._element
		node._element = e
		return e

	def _delete(self, p):
		node = self._validate(p)
		if self.num_children(p) == 2:
			raise ValueError('p has two children')
		child = node._left if node._left else node._right
		if child is not None:
			child._parent = node._parent
		if node is self._root:
			self._root = child
		else:
			parent = node._parent
			if node is parent._left:
				parent._left = child
			else:
				parent._right = child
		self._size -= 1
		node._parent = node
		return node._element


	def _attach(self, p, t1, t2):
		node = self._validate(p)
		if not self.is_leaf(p): 
			raise ValueError('position must be leaf')
		if not type(self) is type(t1) is type(t2): # all 3 trees must be same type
      		# convention for deprecated node
      		raise TypeError('Tree types must match')
      	self._size += len(t1) + len(t2)
      	#...


    def preorder(self):
		if not self.is_empty():
			for p in self._subtree_preorder(self.root)
				yield p

	def _subtree_preorder(self, p):
		yield p
		for c in self.children(p):
			for other in self._subtree_preorder(c):
				yield other


	def postorder(self):
		if not self.is_empty():
			for p in self._subtree_preorder(self.root)
				yield p

	def _subtree_postorder(self, p):
		
		for c in self.children(p):
			for other in self._subtree_postorder(c):
				yield other
		yield p



	def inorder(self):
		if not self.is_empty():
			for p in self._subtree_inorder(self.root)
				yield p

	def _subtree_inorder(self, p):
		if self.left(p) is not None: # if left child exists, traverse its subtree
			for other in self._subtree_inorder(self.left(p)): 
				yield other





		