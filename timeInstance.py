class Time:
    def __init__(self, hour, min, sec, *day):
        self.hour = hour
        self.min = min
        self.sec = sec
        self.day = day
        
    def return_sec(self):
        return (self.hour*60*60) + (self.min*60) + self.sec
    
    def __add__(self, other): # +
        
        total = self.return_sec() + other.return_sec()
        day = int(total/86400)
        total-=(day*86400)
        hour = int(total/3600)
        total-=(hour*3600)
        min = int(total/60)
        total -= (min*60) 
        sec = total

        return Time(hour, min, sec, day)

    def __sub__(self, other): # -
        total = self.return_sec() - other.return_sec()
        day = int(total/86400)
        total-=(day*86400)
        hour = int(total/3600)
        total-=(hour*3600)
        min = int(total/60)
        total -= (min*60) 
        sec = total
        return Time(hour, min, sec,day)
    
    def __lt__(self, other): # <
        return self.return_sec() < other.return_sec()
    
    def __gt__(self, other): # >
        return self.return_sec() > other.return_sec()
    
    def __eq__(self, other): # =
        return self.return_sec() == other.return_sec()
    
    def __repr__(self):
        
        return "{day}일 {hour}시 {min}분 {sec}초 입니다.".format(self.day, self.hour, self.min, self.sec)


hour = int(input("시 입력 : "))
min = int(input("분 입력 : "))
sec = int(input("초 입력 : "))
first_time = Time(10, 10, 10)
second_time = Time(hour, min, sec)
add_time = first_time + second_time
sub_time = first_time - second_time
print("두 시간의 합은")
print(add_time)
print("두 시간의 차는")
print(sub_time)
if (first_time > second_time):
    print("첫번째 시간이 늦은 시간입니다")
if (first_time < second_time):
    print("첫번째 시간이 이른 시간입니다")
if (first_time == second_time):
    print("두 시간이 같은 시간입니다")