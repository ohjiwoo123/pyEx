import sys

s=input("16진수를 입력 하시오") 

value = 0  # 계산 결과 저장 

v = 0   # 변환된 숫자 저장 

i = 0 # i=0 중복문 기준 

r=s[::-1] # s를 역으로 변환 

print(r)
# while (i<len(s)):
#     for c in s: 

#         if (c>='0' and c<= '9') : 

#             v= ord(c)-ord('0')      #  해당되는 숫자 (10진수)  또는    v= int(c)  

#         elif (c>='A' and c<='F') : 

#             v = ord(c)-ord('A')+10     # 해당되는 숫자 (16진수)     

#         else: 

#             print("16진수가 아닙니다.") 

#             sys.exit(0) 


# value = 16**i + v  


# print("16진수 {0} 는 10진수 {1} 입니다".format(s, value)) 