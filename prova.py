c = 2
d = 5

a = int(input('Inserisci il valore: '))

if a > 10:
    b = a - (c + d)
elif a < 5:
    b = a + (c + d)
else:
    b = a + c - d 

print('a: {}' .format(a))
print('b: {}' .format(b))
print('c: {}' .format(c))
print('d: {}' .format(d))
print('Sono del secondo branch')