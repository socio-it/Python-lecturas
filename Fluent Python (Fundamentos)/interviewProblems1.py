#interview problems 
def div(num,den):
    number = 0
    for i in range(num):
        for j in range(den):
            number = i + number
        if(number + num%den == num):
            return i
        else:
            number = 0

print(div(8,4))
print(div(9,4))