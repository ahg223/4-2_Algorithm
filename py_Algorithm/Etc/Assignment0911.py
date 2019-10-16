
file = open("data.txt","r")

Temp=file.read().splitlines()
A=[]

for i in range(0,500):
   A.append(int(Temp[i]))

for i in range(0,499):
   for j in range(0,500):
      if A[i] > A[j]:
         temp=A[i]
         A[i]=A[j]
         A[j]=temp

for i in range(0,100):
   print(A[i])
