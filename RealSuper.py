#부모클래스(추상 메소드)
class Compare():
    def __init__(self, s,t): #상속
        self.s = s
        self.t = t
    def compare(self):  #추상메소드
        pass

#자식클래스3
class fcmp(Compare):
    def compare(self):
        i=0
        num =0
        #s에 문자가 있는지 확인 
        while (i<len(self.s)):  
            #s[i]가 숫자면 다음 문자 체크
            if(self.s[i]>='0' and self.s[i] <= '9'): 
                i= i + 1
                continue
            #s[i]가 -또는 .이면 다음 문자 체크
            elif(self.s[i]=='-' or self.s[i] =='.'):
                i= i + 1
                continue
            #s[i]가 문자임을 확인
            else: 
                num = num+1
                break
        #num이 1이면 strcmp를 반환한다.
        if(num==1):
            return Strcmp
        # s가 숫자일 때
        else:
            # t에 문자가 있는지 확인 
            while(i<len(self.t)):
                #t[i]가 숫자면, 다음 문자 체크 
                if (self.t[i]>='0' and self.t[i]<='9'):
                    i=i+1
                    continue
                elif(self.t[i]=='-' or self.t[i]=='.'):
                    i= i+1
                else:
                    num = num+1
                    break
        #s와 t가 모두 숫자임
        if (num==0):
            return numcmp
        else:
            return strcmp


def strcmp(s,t):
    # 코드 작성
    i=0
    # 앞의 문자열만 비교
    print(len(s),len(t))
    for i in range(min(len(s),len(t))):
        a,b = ord(s[i]),ord(t[i])
        if (a>b):
            return 1
        if (a<b):
            return -1
        else:
            continue
    if (len(s) > len(t)):
        return 1
    elif len(s) < len(t):
        return -1
    else: 
        return 0 

def numcmp(s,t):
    # 코드 작성
    s=float(s)
    t=float(t)
    if (s>t):
        return 1
    if (s<t):
        return -1
    else:
        return 0
        



#비교할 두 값 넣기
s = str(input("첫번째 비교할 값 : "))
t = str(input("두번째 비교할 값 : "))

#객체p생성
p= fcmp(s,t)

print( str(p.compare()) )

