my_list = [1,2,3]

try:
    print("첨자를 입력하세요.")
    index=int(input())
    print(my_list[index])
    if(index==1 or 2):
        print(my_list[index]/0)
    else:
        print(my_list[index])

except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다.({0})".format(err))

except IndexError as err:
    print("잘못된 첨자입니다.({0})".format(err))

else:
    print("except절 만나지 않을 경우 실행됨!")

finally:
    print("나는 마지막에 무조건 나온다.")