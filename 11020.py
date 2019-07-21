def compare(A,B,count):
	answer = 0

	for i in range(len(A)):
		if A[i] != B[i+count]: answer+=1

	return answer


A,B = input().split()

Answer = 101
for i in range(len(B)-len(A)+1):
	temp = compare(A,B,i)
	if Answer>temp: Answer=temp

print(Answer)
