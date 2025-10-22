
def decorator(fun):
    ls = []
    def inter(*args,**kwargs):
        f = fun(*args,**kwargs)
        ls.append(fun)
        print(ls)
        return ls
    return inter

@decorator
def test(x):
    print(x)

test(5)
test(3)
test(2)