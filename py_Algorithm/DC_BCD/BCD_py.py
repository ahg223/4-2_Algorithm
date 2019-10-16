def BCD(Num):
    a=int(Num);
    tmp=[0,0,0,0]
    
    if a-8>=0:
        tmp[0]=1
        a-=8
    
    if a-4>=0:
        tmp[1]=1
        a-=4
    
    if a-2>=0:
        tmp[2]=1
        a-=2
    
    if a-1>=0:
        tmp[3]=1
        a-=1
    
    for i in range(4):
        print("%d" %(tmp[i]), end='')
    
    print(" ", end='')



Num=input("BCD로 출력할 십진법 수를 입력하시오")

for i in Num:
    if "0"<=i<="9":
        BCD(i)
    else:
        print("Error")
        break


