# -*- coding:utf-8 -*-
__author__ = 'apple'
class maketree:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
tree=maketree('A',maketree('B',maketree('E'),maketree('F')),maketree('C',right=maketree('G',maketree('H'))))
def pre(tree):
    if tree==None:
        return
    else:
        print tree.data
        pre(tree.left)
        pre(tree.right)

def mid(tree):
     if tree==None:
         return
     else:
         mid(tree.left)
         print tree.data
         mid(tree.right)

def post(tree):
    if tree==None:
        return
    else:
        post(tree.left)
        post(tree.right)
        print tree.data

pre(tree)
print '------------------'
mid(tree)
print '------------------'
post(tree)
print '------------------'


prelist=list('ABEFCGH')
midlist=list('EBFACHG')
postlist=[]
#利用前序和中序得到后序
def findpost(pre,mid,post):
    if len(pre)==0:
        return
    if len(pre)==1:
        post.append(pre[0])
        return
    root=pre[0]
    n=mid.index(root)
    #houxu
    findpost(pre[1:n+1],mid[:n],post)
    findpost(pre[n+1:],mid[n+1:],post)
    post.append(root)
    return post
print findpost(prelist,midlist,postlist)

def findpre(post,mid,pre):
    if len(post)==0:
        return
    if len(post)==1:
        pre.append(post[-1])
        return
    root=post[-1]
    n=mid.index(root)
    #qianxxu
    pre.append(root)
    findpre(post[:n],mid[:n],pre)
    findpre(post[n:-1],mid[n+1:],pre)
    return pre
postl=list('EFBHGCA')
midl=list('EBFACHG')
prel=[]
print findpre(postl,midl,prel)
