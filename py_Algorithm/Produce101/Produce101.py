#!/usr/bin/env python
# coding: utf-8

# 파일 인풋

# In[1]:


try:
    import openpyxl
except ModuleNotFoundError as E:
    print("해당 컴퓨터에 openpyxl 라이브러리가 있어야 동작합니다!")


# 데이터 읽기

# In[2]:


Data=[]
Tmp=openpyxl.load_workbook('Data.xlsx')
Excel=Tmp.active

for menu1 in Excel.rows:
    i=0
    temp=[]
    for menu0 in menu1:
        temp.append(menu1[i].value)
        i+=1
    Data.append(temp)

    
Data.pop(0)
#print(Data)


# In[4]:


count=1
index=0

while count!=9:
    print("%d week"%count) 
    index=int(input("댄스(1), 보컬(2), 비주얼(3), 정치력(4), 랩(5) 중 어떤 수업을 진행하겠습니까?"))

    for i in Data:
        if (10>i[index]>0): i[index]+=1
    Answer=sorted(Data,key=lambda i:i[1]*i[2]*i[3]*i[4]*i[5], reverse=True)
    
    if count==8: print("축하합니다. 대뷔조는 다음과 같습니다")
    for i in range(11):
        print(Answer[i])
    count+=1


# In[ ]:




