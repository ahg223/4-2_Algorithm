T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length, num=map(int, input().split())
    List=[i for i in range(length+1)]
    List[0]=test_case
    List2=list(map(int, input().split()))
    for i in range(num): List.pop(List.index(List2.pop(0)))
    print("#",end="")
    for i in range(length-num+1): print(List[i],end=" ")
    print()
