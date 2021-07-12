import re
# abcd, book, desk
# ca?e
# cane, cake, cafe, cave
# caae, cabe, cace, cade, ...

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > cane, cake, cafe(O) | caffe (x)
# ^ (^de) : 문자열의 시작 > deer, delay (O) | blonde (x) 
# $ (se$) : 문자열의 끝 > rose, pose (O) | pace (x)

# m = p.match("caffe")
# print(m.group()) # 매치되지 않으면 에러가 발생
def print_match(m):
    if m :
        print(m.group())
    else:
        print("매칭되지 않음")

m = p.match("careless")
print_match(m)