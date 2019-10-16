answer = 0
N = int(input())
for i in range(N):
    Dice = [0]
    temp = list(map(int, input().split()))
    for i in range(1,7): Dice.append(temp.count(i))
    
    Max = max(Dice)
    if Max == 4: award = 50000 + Dice.index(Max) * 5000
    elif Max == 3: award = 10000 + Dice.index(Max) * 1000
    else:
        count, Max, temp = 0, 0, []
        for i in range(1,7):
            if Dice[i] == 2: 
                count+=1
                temp.append(i)
            if Dice[i] == 1: Max = i

        if count == 0: award = Max * 100
        elif count == 1: award = 1000 + temp[0]*100
        else: award = 2000 + temp[0]*500 + temp[1]*500

    if award>answer: answer = award
print(answer)
