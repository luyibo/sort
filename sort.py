__author__ = 'lyb'
import random
import time
l=[random.randint(-100,100) for i in range(100)]
def insert(l):
    for i in range(1,len(l)):
        tmp=l[i]
        j=i-1
        while j>=0 and tmp<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=tmp
    return l

def bubble(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

def quick(l):
    if l==[]:
        return []
    else:
        tmp=l[0]
        lesser=quick([x for x in l[1:] if x<tmp])
        greater=quick([x for x in l[1:]if x>=tmp])
        return lesser+[tmp]+greater

def shell(l):
    n=len(l)/2
    while n>0:
        for i in range(n,len(l)):
            tmp=l[i]
            j=i
            while j>=n and tmp<l[j-n]:
                l[j]=l[j-n]
                j-=n
            l[j]=tmp
        n/=2
    return l

def select(l):
    for i in range(len(l)-1):
        n=l.index(min(l[i:]))
        if n!=i:
            l[n],l[i]=l[i],l[n]
    return l

def makeheap(l,i,k):
    n=k-1
    while 2*i<=n:
        j=2*i
        if j<n and l[j]<l[j+1]:
            j+=1
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
            i=j
        else:break
def heap(l):
    n=len(l)-1
    for i in range(n//2,0,-1):
        makeheap(l,i,len(l))
    while n>1:
        l[n],l[1]=l[1],l[n]
        makeheap(l,1,n)
        n-=1
    return l

def merge(left,right):
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
def mergesort(l):
    if len(l)<=1:
        return l
    else:
        mid=len(l)/2
        left=mergesort(l[:mid])
        right=mergesort(l[mid:])
        return merge(left,right)
print insert(l)
print bubble(l)
print quick(l)
print shell(l)
print select(l)
print heap(l)
t1=time.time()
print mergesort(l)
t2=time.time()
print t2-t1
t3=time.time()
l.sort()
print l
t4=time.time()
print t4-t3