#Stack implementation
def parentheses_balanced(s):
    a = []
    for x in list(s):    
        if x == '(':
            a.append(x)
        elif x == ')':
            if len(a) == 0:
                return False
            else:
                a.pop(-1)
    return True

a = '(()()))'
print(parentheses_balanced(a))