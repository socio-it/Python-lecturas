import random
text = \
"""
x  =  5  , 200
y  =  5  , 230
z  =  5  , 240
"""
name = slice(0,1)
number = slice(6,7)
lines_items = text.split('\n')
for item in lines_items:
    print(item[name], item[number])

print(random.choice(range(500)))