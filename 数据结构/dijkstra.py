# -*- coding:utf-8 -*-
__author__ = 'apple'
_=float('inf')
def dijkstra(graph,n):
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
            if dis[i]>dis[k]+graph[k][i]:
                dis[i]=dis[k]+graph[k][i]
                pre[i]=k
    return dis,pre
n=6
graph=[
    [0,4,3,_,_,_],
    [4,0,2,1,_,_],
    [3,2,0,3,4,_],
    [_,1,3,0,2,3],
    [_,_,4,2,0,1],
    [_,_,_,3,1,0]
]
dis,pre=dijkstra(graph,n)
print dis
print pre
#1.求出A到其他点的最小路径
#2.先求出A到相邻点的路径，得到最小距离，即C，然后求出A经C到C相邻点的距离
#3.以此类推，得到所有点的最小路径