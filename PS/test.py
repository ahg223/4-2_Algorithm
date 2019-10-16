score = [['이효리', 2011001001, {'국어':94, '영어':91, '수학':89, '과학':83}],
        ['아이유', 2014001002, {'국어':99, '영어':90, '수학':86, '과학':81}],
        ['엄정화', 2008001003, {'국어':80, '영어':70, '수학':76, '과학':65}],
        ['박나래', 2015001004, {'국어':100, '영어':89, '수학':72, '과학':69}]]

for i in range(4):
    average = 0
    dic = score[i][2]

    for subject in dic.keys(): average+=dic[subject]
    print(average/len(dic))
####################################################

for i in range(4):
    average = 0
    dic = score[i][2]

    for key,value in dic.items(): average+=value
    print(average/len(dic))

#####################################################

subject = ['국어','영어','수학','과학']

average = score[0][2][subject[0]] + score[0][2][subject[1]] + score[0][2][subject[2]] + score[0][2][subject[3]]
print(average/4)

average = score[1][2][subject[0]] + score[1][2][subject[1]] + score[1][2][subject[2]] + score[1][2][subject[3]]
print(average/4)

average = score[2][2][subject[0]] + score[2][2][subject[1]] + score[2][2][subject[2]] + score[2][2][subject[3]]
print(average/4)

average = score[3][2][subject[0]] + score[3][2][subject[1]] + score[3][2][subject[2]] + score[3][2][subject[3]]
print(average/4)
