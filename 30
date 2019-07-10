Num = input()

Flag = False
Answer = 0

for i in range(len(Num)):
	#print(Num[i],Answer)
	if Num[i] == "0": Flag = True
	Answer += int(Num[i])

if Flag and Answer%3 ==0:
	Answer = list(Num)
	Answer.sort(reverse = True)
	for i in range(len(Answer)):
		print(Answer[i], end="")
	print()

else: print(-1)
