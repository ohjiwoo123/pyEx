s=list(input("대상 문자열 입력"))
t=list(input("제거할 문자 입력"))

ss="".join(map(str, s))
tt="".join(map(str, t))
c = s.count(tt)
print(c)

for i in range(0,c):
    d=s.index(tt)
    s.pop(d)

print(s)
s.reverse()
print(s)
result=s
print("결과 리스트는 {0}입니다.".format(result))

# def merge_string(*s):
#     result = ''
#     for i in s:
#         result = result+i
#         return result

# g = merge_string(s)
# print(g)