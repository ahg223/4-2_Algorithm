def find_lower_bound(mat,job,row,n):
    k=0
    for i in range(row+1,n):
        min = 10000000
        for j in range(0,n):
            if job[j]==0 and mat[i][j] < min:
                min=mat[i][j]
        k+=min
    return k

def job_assinging(mat,mat2,job,row,choice,sol,n):
    for i in range(0,n):
        if job[i]==0:
            job[i]=1
            temp = find_lower_bound(mat,job,row,n)
            mat2[row][i]=choice+mat[row][i]+temp
            job[i]=0
    if row+2==n:
        for i in range(0,n):
            if mat2[row][i]!=0 and mat2[row][i]<sol[0]:
                sol[0]=mat2[row][i]
        return
    for k in range(1,n+1):
        if job[k-1]:
            continue
        temp_index=-1
        temp=10000000
        for i in range(0,n):
            if mat2[row][i]!=0 and mat2[row][i]<temp:
                temp = mat2[row][i]
                temp_index = i
        if mat2[row][temp_index]<sol[0]:
            choice=choice+mat[row][temp_index]
            job[temp_index]=1
            row=row+1
            job_assinging(mat,mat2,job,row,choice,sol,n)
            job[temp_index]=0
            row = row-1
            choice = choice-mat[row][temp_index]
            for i in range(row+1,n):
                for j in range(0,n):
                    mat2[i][j]=0
        mat2[row][temp_index]=0

matrix = []
matrix2 = []
job1 = []
temp_list =[]
answer=[10000000]

n=int(input("Typing value of n : "))
for i in range(0,n):
    temp_list.append(0)
    job1.append(0)
    
for i in range(0,n):
    matrix.append(temp_list[:])
    matrix2.append(temp_list[:])
print(job1)
print("")
for i in range(0,n):
    for j in range(0,n):
        temp=int(input("%Typing dst person's cost of %dst job : " %(i+1,j+1)))
        matrix[i][j]=temp
if n==1:
    print("\nTotal cost is %d\n" %matrix[0][0])
else:
    job_assinging(matrix,matrix2,job1,0,0,answer,n)
    print("\nTotal cost is %d\n" %answer[0])
