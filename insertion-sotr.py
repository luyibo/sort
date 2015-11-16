#coding=utf-8
__author__ = 'lyb'
A=[5,2,4,6,1,3]
for j in range(1,len(A)):
    key=A[j]
    i=j-1
    while i>=0 and A[i]>key:
        A[i+1]=A[i]
        i-=1
    A[i+1]=key
#print A


a=[13,-3,-25,-20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
start=a[-1]
all=a[-1]
for i in a[::-1][1:]:
    if start<0:
        start=0
    start+=i
    if all<start:
        all=start
print  all
start=a[0]
all=a[0]
for i in a[1:]:
    if start<0:
        start=0
    start+=i
    if all<start:
        all=start
#print all
nums=[1,2,3,3]
target=3

if len(nums)==0:
            b=[-1,-1]
elif len(nums)==1:
             b=[0,0]
else:
            a=[]
            for i in range(len(nums)):
                if target==nums[i]:
                    a.append(i)
                    print a
            b=[min(a),max(a)]
print b

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def pre(root):
    if root==None:
        return
    print root.data
    pre(root.left)
    pre(root.right)

def mid(root):
    if root==None:
        return

    mid(root.left)
    print root.data
    mid(root.right)
def past(root):
    if root==None:
        return
    past(root.left)
    past(root.right)
    print root.data
root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'),Node('H'))))
pre(root)
print('\n')
def find(root,x):
    if root!=None:
        if root.data==x:
            return x
        find(root.left,x)
        find(root.right,x)
    else: return None

print find(root,'G')

preList=list('DBACEGF')
midList=list('ABCDEFG')
afterList=[]

def findtree(preList,midList,afterList):
    if len(preList)==0:
        return
    if len(preList)==1:
        afterList.append(preList[0])
        return
    root=preList[0]
    n=midList.index(root)
    findtree(preList[1:n+1],midList[:n],afterList)
    findtree(preList[n+1:],midList[n+1:],afterList)
    afterList.append(root)

def findpre(last,mid,l):
    if len(last)==0:
        return
    if len(last)==1:
        l.append(last[-1])
        return
    root=last[-1]
    n=mid.index(root)
    l.append(root)
    findpre(last[:n],mid[:n],l)
    findpre(last[n:-1],mid[n+1:],l)


    return l
last=list('DBFGECA')
mid=list('BDAFEGC')
l=[]
print findpre(last,mid,l)

class t:
    def __init__(self,left,right):
        self.left=left
        self.right=right
def huffman(l):

    while len(l)>=2:

       a=l[0]+l[1]
       b=l.pop(0)
       c=l.pop(0)
       t.left=a
       t.right=b



l=[1,2,4,6,9,14]
huffman(l)


