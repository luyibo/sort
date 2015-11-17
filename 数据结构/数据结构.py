# -*- coding:utf-8 -*-
__author__ = 'apple'
class Stack:
    def __init__(self,size):
        self.stack=[]
        self.top=-1
        self.size=size
    def isempty(self):
        if self.top==-1:
            return True
        else:return False
    def push(self,x):
        if self.isfull():
            raise Exception("StackIsFull")
        else:
            self.stack.append(x)
            self.top+=1
        return self.stack
    def isfull(self):
        if self.top==self.size-1:
            return True
        else:return False
    def pop(self):
        if self.isempty():
            raise Exception('StackIsEmpty')
        else:
            self.stack.pop()
            self.top-=1

class Queue():
    def __init__(self,size,head=0,tail=0):
        self.size=size
        self.queue=[]
        self.head=head
        self.tail=tail
    def isempty(self):
        if self.tail==self.head:
            return True
        else:return False
    def isfull(self):
        if self.tail+1==self.head:
            return True
        else:return False
    def enqueue(self,object):
        if self.tail==self.size-1:
                self.tail=-1
        else:
                self.tail+=1
        if self.isfull():
            raise Exception('QueueIsFull')
        else:
            self.queue.append(object)

    def dequeue(self):
        if self.isempty():
            raise Exception('QueueIsEmpty')
        else:
            x=self.queue[self.head]
            if self.head==self.size-1:
                self.head=0
            else:self.head+=1


class BinaryTree():
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
class BT:
    def __init__(self):
        self.root=None
    def makeTree(self,data,left=None,right=None):
        self.root=BinaryTree(data,left,right)
    def preorder(self,r):
        if r.root is not None:
            print(r.root.data)
            if r.root.left is not None:
                self.preorder(r.root.left)
            if r.root.right is not None:
                self.preorder(r.root.right)
    def inOrder(self,r):
        if r.root is not None:
            if r.root.left is not None:
                self.inOrder(r.root.left)
            print r.root.data
            if r.root.right is not None:
                self.inOrder(r.root.right)
    def postOrder(self,r):
        if r.root is not None:
            if r.root.left is not None:
                self.postOrder(r.root.left)
            if r.root.right is not None:
                self.postOrder(r.root.right)
            print r.root.data

r = BT()
ra = BT()
rb = BT()
rc = BT()
rd = BT()
re = BT()
rf = BT()
rg = BT()
rh = BT()
r.makeTree(1)
ra.makeTree(2)
rb.makeTree(3,ra,r)
rc.makeTree(4)
rd.makeTree(5)
re.makeTree(6,rc,rd)
rf.makeTree(7,re)
rg.makeTree(8,rb)
rh.makeTree(9,rf,rg)
rh.preorder(rh)
return