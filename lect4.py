#Sorry Iva! It was my fault. The second "p = ..." was on wrong position. Ewrething now is OK. But this error is on the website https://zazloo.ru/modul-4-2-pokolenie-python/
# Early in the morning I didn't see it.
a = int(input('enter digit: '))
if a > 2 and a < 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
    p = (a + b) * (a + b)
print(p)
