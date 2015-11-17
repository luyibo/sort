# -*- coding:utf-8 -*-
__author__ = 'apple'
import time
def binarysearch(l,n):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)/2

        if n==l[mid]:
                return mid
        elif n<l[mid]:
                high=mid-1
        else:
                low=mid+1


l=[1,4,7,9,14,34,76,100,101]
n=100
#print binarysearch(l,n)

def goldsearch(l,n):
    low=0
    high=len(l)-1
    while low<=high:
        mid=int(low+0.618*(high-low+1)-1+0.5)
        if n==l[mid]:
            return mid
        else:
            if n>l[mid]:
                low=mid+1
            else:
                high=mid-1

print goldsearch(l,n)

def precisesearch(l,n):
    low=0
    high=len(l)-1
    mid=low+(n-l[0])*(high-low)/(l[-1]-l[0])
    if n==l[mid]:
        return mid
    else:
        if n<l[mid]:
            while n<l[mid]:
                mid-=1
            if l[mid]==n:
                return mid
        else:
            while l[mid]<n:
                mid+=1
            if l[mid]==n:
                return mid
print precisesearch(l,n)
#(mid-low)/(high-low)=(k-l[low])/(l[high]-l[low])
# mid=low+(n-l[0])*(high-low)/(l[-1]-l[0])
