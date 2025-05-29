#Jasmeen Kaur, tree.py

from stack import Stack
class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    #left node in tree

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
            #adds left
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode): #similar to insert left function
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        #adds right child
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild
        #returns right child

    def getLeftChild(self):
        return self.leftChild
        #returns left child (same as right child function)

    def setRootVal(self,obj):
        self.key = obj
        # value is set to obj

    def getRootVal(self):
        return self.key
        #returns that value

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s


class ExpTree(BinaryTree):
    def make_tree(postfix):
        stack = Stack()
        symbols = set(["+", "-", "*", "/", "^"])
        for x in postfix:
            #is it a digit?
            if x in symbols:
                temp = ExpTree(x)
                temp.rightChild = stack.pop()
                temp.leftChild = stack.pop()
                stack.push(temp)
            else:
                stack.push(ExpTree(x))            
        return stack.pop()

    def preorder(tree):
        s = ''
        #is tree empty
        if tree:
            s = tree.getRootVal()

            s += ExpTree.preorder(tree.getLeftChild())

            s += ExpTree.preorder(tree.getRightChild())
        return s

#recursion in both 
    def inorder(tree):
        s = ''
        if tree is not None:
            if tree.getLeftChild() is None and tree.getRightChild() is None:
                s += str(tree.getRootVal())
            else:
                s += "("
                s += ExpTree.inorder(tree.getLeftChild())
                s += str(tree.getRootVal())
                s += ExpTree.inorder(tree.getRightChild())
                s += ")"
        return s

    def postorder(tree):
        s = ''
        # checks to see if tree is empty
        if tree:
            # traverses left subtree recursively
            s += ExpTree.postorder(tree.getLeftChild())
            # traverses right subtree recursively
            s += ExpTree.postorder(tree.getRightChild())
            # prints root node
            s += str(tree.key)
        return s

    def evaluate(tree):
        symbols = ["+","-","*","/","^"]
        if tree is None:
            return None

        root = tree.getRootVal()
        if root not in symbols:
            return float(root)
        
        left = ExpTree.evaluate(tree.getLeftChild())
        right = ExpTree.evaluate(tree.getRightChild())

        #making new digits floats

        l = float(left)
        r = float(right)

        if root == "+":
            return l + r
        elif root == "-":
            return l - r
        elif root == "*":
            return l * r
        elif root == "/":
            return l / r
        elif root == "^":
            return l ** r
        else:
            return None
        

    def __str__(self):
        return ExpTree.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'
    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0