def deco(func):
    def deco_func(*args, **kwargs):
        print("decorate")
        return func(*args,**kwargs)
    return deco_func


@deco
def original_func():
    print("original")
original_func()


#stricmp(s,t)   // 공백은 무시하고 비교