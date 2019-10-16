Test_case = int(input())

for _ in range(Test_case):
	Person = []
	Answer = 0
	N = int(input())

	for _ in range(N):Person.append(list(map(int,input().split())))
	
	Person.sort(key=lambda x:x[0])
	
	speech = 1000000
	for i in range(N):
		if speech>Person[i][1]: 
			speech = Person[i][1]
			Answer +=1
	print(Answer)
		
