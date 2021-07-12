#부모클래스의 compare추상메소드로, 자식클래스 메소드인 strcmp, numcmp 2개 오버라이딩
#들어온값이 문자열이면 strcmp
#들어온값이 숫자인 문자열이면 numcmp

#부모클래스(추상 메소드)
class Compare ():
    def __init__(self, s,t): #상속
        self.s = s
        self.t = t
    def compare(self):  #추상메소드
        pass
    
#자식클래스1
class Strcmp(Compare):
    def compare(self):  #오버라이딩
        if self.s>self.t:
            return 1
        elif self.s<self.t:
            return -1
        else:
            return 0

#자식클래스2
class Numcmp(Compare):
    def compare(self):  #오버라이딩
        if float(self.s)>float(self.t):
            return 1
        elif float(self.s)<float(self.t):
            return -1
        else:
            return 0


#비교할 두 값 넣기
s = str(input("첫번째 비교할 값 : "))
t = str(input("두번째 비교할 값 : "))


#객체p생성
if s.isdigit() and t.isdigit():   #둘다 전부 숫자일때 
    p = Numcmp(s,t)
else:                               #문자가 하나라도 섞여있으면
    p = Strcmp(s,t)

print( p.compare() )

