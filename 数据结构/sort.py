# -*- coding:utf-8 -*-
__author__ = 'apple'
import sys
sys.setrecursionlimit(1000000)
import time
import random
def insert(l):
    for i in range(1,len(l)):
        tmp=l[i]
        j=i-1
        while j>=0 and tmp<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=tmp
    return l
l=[random.randint(-100,100) for i in range(10000)]
def shellsort(l):
    n=len(l)
    while n>=1:
        for i in range(n,len(l)):
            tmp=l[i]
            j=i
            while j>=n and tmp<l[j-n]:
                l[j]=l[j-n]
                j-=n
            l[j]=tmp
        n=n/2
    return l

t3=time.time()
shellsort(l)
t4=time.time()
print t4-t3
def bubble(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                print  l

t1=time.time()
bubble(l)
t2=time.time()
print t2-t1

def bubbleSort(a):
    l=len(a)-2
    i=0
    while i<l:
        j=l
        while j>=i:
            if(a[j+1]<a[j]):
                a[j],a[j+1]=a[j+1],a[j]
            j-=1
        i+=1

    return l

t5=time.time()
bubbleSort(l)
t6=time.time()
print t6-t5

def quicksort(l):
    if l==[]:
        return []
    else:
        tmp=l[0]
        lesser=quicksort([x for x in l[1:] if x<tmp])
        greater=quicksort([x for x in l[1:] if x>=tmp])
        return lesser+[tmp]+greater
t7=time.time()
quicksort(l)
t8=time.time()
print t8-t7

def mergesort(seq):
    if len(seq)<=1:
        return seq
    mid=int(len(seq)/2)
    left=mergesort(seq[:mid])
    right=mergesort(seq[mid:])
    return merge(left,right)

def merge(left,right):
    result=[]
    i,j=0,0
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
t9=time.time()
mergesort(l)
t10=time.time()
print t10-t9
t11=time.time()
l.sort()
t12=time.time()
print t12-t11