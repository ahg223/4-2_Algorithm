#Factiorial

N=int(input("몇 번째 팩토리얼 숫자를 원하시나요?"))

M=1
F=1

while M != N:
   M=M+1
   F=F*M

print(F, "가 해당하는 숫자입니다")
