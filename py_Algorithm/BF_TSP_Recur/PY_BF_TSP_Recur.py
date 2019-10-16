#!/usr/bin/env python
# coding: utf-8

# TSP Brutal Force by Recursive

# In[81]:


INT_MAX = 2147483647
visited=[0 for i in range (11)]
Min=INT_MAX


# In[82]:


def min(x,y):
    if x>y: 
        return y
    else: 
        return x


# In[83]:


def tsp(Next, total, Recur):
    global Min
    global visited
    if Recur==MAX:
        if TSP[Next][1] != 0:
            Min=min(Min,total+TSP[Next][1])
            return
        
    visited[Next]=True;
    for i in range(1,MAX+1):
        if visited[i] == False and TSP[Next][i] != 0:
            tsp(i,total+TSP[Next][i],Recur+1)
            
    visited[Next]=False


# In[85]:



MAX=int(input("How many city in there? "))
TSP = [[0]*(11) for i in range(11)]

for i in range(1,MAX+1):
    for j in range(1,MAX+1):
        TSP[i][j]=int(input())

tsp(1,0,1)
print(Min)

