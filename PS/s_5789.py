T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print("#",end="")
    print(test_case,end=" ")
    length, num=map(int,input().split())
    List=[0 for _ in range(length)]
    for i in range(1,num+1):
        start, end= map(int,input().split())
        for _ in range(start-1,end): List[_]=i
            
    for i in range(length): print(List[i],end=" ")
