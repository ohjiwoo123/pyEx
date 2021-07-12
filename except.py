class MyException(Exception):
    pass

class MyException(Exception):
    def __init__(self):
        super().__init__("MyException이 발생하였습니다.")