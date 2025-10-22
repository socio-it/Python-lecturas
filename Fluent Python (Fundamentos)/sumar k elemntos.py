
n = [1, 2, 3, 4,5,7]


def find_same_T(s,T):
    h = len(s)
    c = None
    if h > 0:
        mid= h // 2 + h % 2
        if s[mid-1] == T:
            c = s[mid-1]
        if s[mid-1] < T:
            c = find_same_T(s[mid:], T)
    return c


def sum(j,c,s,T,k):
    h = len(s)
    k -= 1
    for x in range(h):
        print(k, ';',s[x])
        c.append(s[x])
        if s[x]<= T:
            diff = T - s[x]
            print(k, ';:',diff)
            if k > 1:
                sum(j,c,s[x+1:],diff,k)
            else:
                res = find_same_T(s[x:],diff)
                if res:
                    c.append(res)
                    print('find',res,' res',c)
                    j.append(c[:])
                    c.pop()
        c.pop()

def sum_k(s,T,k):
    c=[]
    x=[]
    sum(x,c,s,T,k)
    return x

print(find_same_T(n, 3))

print(sum_k(n,12,2))
