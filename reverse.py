def revsqueeze(s,t):
    ss="".join(map(str, s))
    tt="".join(map(str, t))
    c = s.count(tt)

    for i in range(0,c):
        d=s.index(tt)
        s.pop(d)


    s.reverse()


s=list(input("대상 문자열 입력"))
t=list(input("제거할 문자 입력"))
revsqueeze(s,t)
result=s
print("결과 리스트는 {0}입니다.".format(result))

