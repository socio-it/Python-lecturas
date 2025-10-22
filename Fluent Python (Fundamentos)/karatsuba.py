def karatsuba(x,y):
    if x<10 or y<10:
        return x*y
    
    n = max(len(str(x)), len(str(y)))
    m = n//2

    a,b = x//(10**m),x%(10**m),
    c,d = y//(10**m),y%(10**m),

    z_0 = karatsuba(b,d)
    z_1 = karatsuba(a+b,c+d)
    z_2 = karatsuba(a,c)

    ans = (z_2 *10**(2*m)) + ((z_1-z_2-z_0) * 10 ** m) + z_0
    
    return ans

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
print(karatsuba(40,50))