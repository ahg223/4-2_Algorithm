#!/usr/bin/env python
# coding: utf-8

# In[4]:


string = input("Typing sentence : ")

string.replace(",", " ")

String = string.split()
dic1 = {}
dic2 = {}

for i in String:
    if i in dic1: dic1[i] += 1
    else: dic1[i] = 0

    for j in i:
        if j in dic2: dic2[j] += 1
        else: dic2[j] = 0

print("Most word : ", max(dic1, key=dic1.get), "\nMost character : ", max(dic2, key=dic2.get))


# In[ ]:




