import sys


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
        
def deco(func):
    def stricmp(*args, **kwargs):
        s= args[0].replace(" ","")
        t= args[1].replace(" ","")
        print(s,t)
        return func(s, t)
    return stricmp
    
@deco    
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

def fcmp(s,t):
    i=0
    num =0
    #s에 문자가 있는지 확인 
    while (i<len(s)):  
        #s[i]가 숫자면 다음 문자 체크
        if(s[i]>='0' and s [i] <= '9'): 
            i= i + 1
            continue
        #s[i]가 -또는 .이면 다음 문자 체크
        elif(s[i]=='-' or s[i] =='.'):
            i= i + 1
            continue
        #s[i]가 문자임을 확인
        else: 
            num = num+1
            break
    #num이 1이면 strcmp를 반환한다.
    if(num==1):
        return strcmp
    # s가 숫자일 때
    else:
        # t에 문자가 있는지 확인 
        while(i<len(t)):
            #t[i]가 숫자면, 다음 문자 체크 
            if (t[i]>='0' and t[i]<='9'):
                i=i+1
                continue
            elif(t[i]=='-' or t[i]=='.'):
                i= i+1
            else:
                num = num+1
                break
    #s와 t가 모두 숫자임
    if (num==0):
        return numcmp
    else:
        return strcmp


s=input("비교할 첫 번째 숫자 또는 문자를 입력하세요.")
t=input("비교할 두 번째 숫자 또는 문자를 입력하세요.")
p = fcmp(s,t)
print(str(p(s,t)))