
Len = int(input())

List = list(map(int, input().split()))
List.sort()

Answer, temp = 0, 0
for i in range(Len):
	temp+=List[i]
	Answer+=temp
print(Answer)
	
