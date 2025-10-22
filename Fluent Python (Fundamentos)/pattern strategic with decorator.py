
funtions = []
def decorator_strategic(fun):      
    funtions.append(fun)

def calMaxTax(x):
    val = 0
    for fun in funtions:
        if val <= fun(x): val = fun(x)
    return val

@decorator_strategic
def tax1(x):
    return x*10

@decorator_strategic
def tax1(x):
    return x*40

print(calMaxTax(2))