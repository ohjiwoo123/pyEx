import sys

s= input("16진수를 입력하세요")
value = 0 # 계산결과 저장
v= 0 # 변환된 숫자 저장
c=list(s)
b=0

for c in s:
    if(c >= '0' and c<='9'):
        v= ord(c) - ord('0')
        b += 1    # 해당되는 숫자 10진수, 문자  '1' - '0' => 49 - 48 = 1 
    elif(c >='A' and c<='F'):
        v = ord(c)-ord('A')+10 # 해당되는 숫자 (16진수) || 문자 B - A +10 = 11이고, 10진수 11은 16진수 0x0B이다.
        b += 1 
    else:
        print("16진수가 아닙니다.")
        sys.exit(0)

for i in v:
    value = v + 16*(b-1)

print(value)

