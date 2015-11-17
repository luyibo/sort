# -*- coding:utf-8 -*-
__author__ = 'apple'
_=float('inf')
def prim(graph,n):
    dis=[0]*n
    pre=[0]*n
    flag=[False]*n
    flag[0]=True
    k=0
    for i in range(n):
        dis[i]=graph[k][i]
    for j in range(n-1):
        mini=_
        for i in range(n):
            if mini>dis[i] and not flag[i]:
                mini=dis[i]
                k=i
        print k
        if k==0:
            return
        flag[k]=True
        for i in range(n):
            if dis[i]>dis[k] and not flag[i]:
                dis[i]=graph[k][i]
                pre[i]=k
    return dis,pre
n=6
graph=[
    [0,6,3,_,_,_],
    [6,0,2,5,_,_],
    [3,2,0,3,4,_],
    [_,5,3,0,2,3],
    [_,_,4,2,0,1],
    [_,_,_,3,1,0]
]
dis,pre=prim(graph,n)
print dis
print pre
#prim算法的步骤
#1.以A为起点，即graph[0]，求出graph[0]中的最小值，即C
#2，在A，C中选择下一跳的最小值，且不会形成环，即B
#3.一次类推，找出所有的边
