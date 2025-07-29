w1 = ''.join(char for char in input() if char.isalnum()).lower()
w2 = ''.join(char for char in input() if char.isalnum()).lower()

d1 = {}
for i in w1:
    d1.setdefault(i, w1.count(i))
del d1[' ']

d2 = {}
for i in w2:
    d2.setdefault(i, w2.count(i))
del d2[' ']


print('YES' if d1 == d2 else 'NO')
print(d1)
print(d2)