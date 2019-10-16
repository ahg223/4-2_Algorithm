
#엑셀 읽어오기
try:
    import openpyxl
except ModuleNotFoundError as E:
    print("해당 컴퓨터에 openpyxl 라이브러리가 있어야 동작합니다!")

allergy=[]
Menu=openpyxl.load_workbook('데이터_셋완성.xlsx')
menu2=Menu.active

for menu1 in menu2.rows:
    row_index=menu1[0].row
    i=0
    temp=[]
    for menu0 in menu1:
        if menu1[i].value ==None:
            break
        temp.append(menu1[i].value)
        i+=1
    allergy.append(temp)

#알레르기 목록 출력
Alist=[]

print("다음 중 해당하는 알레르기를 정수로 입력해주세요!")
print(" 1. 난류 \n 2. 우유 \n 3. 메밀 \n 4. 땅콩 \n 5. 대두 \n 6. 밀 \n 7. 고등어 \n 8. 게 \n 9. 새우 \n 10. 돼지고기 \n 11. 복숭아 \n 12. 토마토 \n 13. 아황산염 \n 종료를 원하시면 0을 입력해주세요.")

while True:
    temp=int(input())

    if temp==0:
        break
    elif 0<temp<14:
        Alist.append(temp)
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

#해당 날짜 입력받은 뒤 섭취 가능 음식 목록 출력
Today=[]
Date=int(input("몇 일의 식단이 궁금하신가요? "))
Answer=[]
flag=0


for i in allergy:
    if i[0]==Date:
        Today.append(i)
        
if Today:

    print("%d일 식단" %Date)
    for i in Today:
        print(i)

    for i in Today:
        num=0
        flag=0
        answer=[]
        for j in i:
            num+=1
            if 1<=num<3:
                answer.append(j)
                continue
            if Alist.count(j)!=0:
                flag+=1
        if flag==0:
            Answer.append(answer)

    print("%d일 알러지를 제외한 식단"%Date)
    for i in Answer:
        print(i)

else:
    print("해당 날짜의 식단이 존재하지 않습니다")
