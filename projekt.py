from collections import deque
from typing import Any, Callable

class BinaryNode:
    def __init__(self, value:Any):
        self.value=value
        self.left_child:BinaryNode=None
        self.right_child:BinaryNode=None
        self.parent:BinaryNode=None


    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        return True

    def add_left_child(self, value):
        self.left_child = BinaryNode(value)
        self.left_child.parent = self

    def add_right_child(self,value):
        self.right_child = BinaryNode(value)
        self.right_child.parent = self

    def traverse_post_order(self, visit:Callable[['Any'],None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)
    def traverse_in_order(self, visit:Callable[['Any'],None]):
        if self.right_child:
            self.right_child.traverse_in_order(visit)
        visit(self)
        if self.left_child:
            self.left_child.traverse_in_order(visit)


    def traverse_pre_order(self,visit:Callable[['Any'],None]):
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

class BinaryTree:
    def __init__(self, root:BinaryNode):
        self.root = root

    def traverse_post_order(self, visit:Callable[['Any'],None]):
        if type(self) is BinaryTree:
            if self.root.left_child:
                self.root.left_child.traverse_post_order(visit)
            if self.root.right_child:
                self.root.right_child.traverse_post_order(visit)
            visit(self.root)
        if type(self) is BinaryNode:
            if self.left_child:
                self.left_child.traverse_post_order(visit)
            if self.right_child:
                self.right_child.traverse_post_order(visit)
            visit(self)

    def traverse_in_order(self, visit:Callable[['Any'],None]):
        if type(self) is BinaryTree:
            if self.root.right_child:
                self.root.right_child.traverse_in_order(visit)
            visit(self.root)
            if self.root.left_child:
                self.root.left_child.traverse_in_order(visit)

        if type(self) is BinaryNode:
            if self.right_child:
                self.right_child.traverse_in_order(visit)
            visit(self)
            if self.left_child:
                self.left_child.traverse_in_order(visit)

    def traverse_pre_order(self,visit:Callable[['Any'],None]):
        if type(self) is BinaryTree:
            visit(self)
            if self.root.left_child:
                self.root.left_child.traverse_pre_order(visit)
            if self.root.right_child:
                self.root.right_child.traverse_pre_order(visit)

        if type(self) is BinaryNode:
            visit(self)
            if self.left_child:
                self.left_child.traverse_pre_order(visit)
            if self.right_child:
                self.right_child.traverse_pre_order(visit)

    def show(self):
        y = "--"
        if type(self) is BinaryTree:
            if self.root.left_child:
                BinaryTree.show(self.root.left_child)
            print(str(self.root.value))
            if self.root.right_child:
                BinaryTree.show(self.root.right_child)
        if type(self) is BinaryNode:
            if self.left_child:
                BinaryTree.show(self.left_child)
            print(y+str(self.value))
            if self.right_child:
                BinaryTree.show(self.right_child)


def visit(node: BinaryNode):
    print(node.value)

def all_path(tr:BinaryTree):
    wynik = [[]]
    x = []
    root = tr.root
    stos = deque()
    stos.append((root, x))
    while stos:
        node,x = stos.pop()

        x.append(node)
        if node.is_leaf():
            wynik.append(list(x))
        if node.right_child:
            stos.append((node.right_child,list(x)))
        if node.left_child:
            stos.append((node.left_child,list(x)))

    return wynik


bn = BinaryNode(10)

bn.add_left_child(9)
bn.add_right_child(7)
bn.left_child.add_left_child(5)
bt = BinaryTree(bn)

bt.show()
lista = all_path(bt)
st = ""
for x in lista:
    print("\n")
    for y in x:
        st+="["+str(y.value)+"]"
    print(st)
    st=""






