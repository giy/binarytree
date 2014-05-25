#!/usr/bin/python
"From Laurent Luce's implementation"

class TreeNode:
    def __init__(self, x):
	self.left = None
	self.right = None
	self.data = x

    def insert(self, data):
	"Insert a new node into the binary tree"
	if data < self.data:
            if self.left is None:
	        self.left = TreeNode(data)
            else:
		self.left.insert(data)
	else:
	    if self.right is None:
	        self.right = TreeNode(data)
	    else:
		self.right.insert(data)

    def lookup(self, data, parent=None):
	"Lookup the node containing data"
	if data < self.data:
	    if self.left is None:
                return None, None
	    return self.left.lookup(data, self)
        elif data > self.data:
	    if self.right is None:
		 return None, None
	    return self.right.lookup(data, self)
        else:
            return self, parent

    def inorder(self):
	"Inorder tree traversal"
	if self.left:
            self.left.inorder()
	print self.data,
	if self.right:
	    self.right.inorder()

    def preorder(self):
	"Preorder tree traversal"
	print self.data,
	if self.left:
	    self.left.preorder()
	if self.right:
	    self.right.preorder()

    def postorder(self):
	if self.left:
	    self.left.postorder()
	if self.right:
	    self.right.postorder()
	print self.data,
	    

root = TreeNode(11)
root.insert(5)
root.insert(12)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
print "\n Inorder"
root.inorder()
print "\n Preorder"
root.preorder()
print "\n Postorder"
root.postorder()
