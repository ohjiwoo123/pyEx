# 실습)주어진 리스트 에서 a번째에서 b개를 취하여 주는 프로그램을 짜시오 

#     - ex) abcdefg  2  3  à  bcd 

#     - 입력은 s=list(input(“대상 문자열 입력”)) 

#              a=int(input(“시작 지점 입력”)) 

#              b=int(input(“취할 갯수 입력”)) 

#    - 결과는 result 리스트에 저장 a

#    - 출력은 print(“결과 문자열은 {0} 입니다”.format(result))   # str(result) 

#    - 1) 슬라이싱, append, + 연산자 사용 

#            - 교재 3장 4, 6page,  5장 10page 참조 

#      2) 완성후에 invalid parameter a & b 체크 항목 추가 할 것 

# - 결과 리스트 만들기 전에 잘못 된 a와 b를 별도로 체크 할 것 

# - a와 b는 1이상인 값이 들어 온다는 전제하에 체크 할 것. 
import sys
s=list(input())
lenthOfS = len(s)
a=int(input())
b=int(input())
if (a and b <=0):
    print("1보다 작은 값을 입력하였습니다.")
    sys.exit(0)
midstr = s[a-1:len(s)]
result = s[a-1:a-1+b]
print("결과 문자열은 {0} 입니다".format(result))
