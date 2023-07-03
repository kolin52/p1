a = 3
b = 4
c = 5 # hipotenuza
print(c**2, ' = ', a**2 + b**2)

# x e hipotenuzata
x = int(c**2)
# y i z sa katetite
y = int(a**2)
z = int(b**2)
x = y + z
print(x)

# moje i po tozi nachin
# h - hipotenuza
h = int( input('vavedete razmera na hipotenuzata: '))
# c1 ediniat katet
c1 = int( input('vavedete razmera na katet 1: '))
# c2 drugiat katet
c2 = int( input('vavedete razmera na katet 2: '))
print(h**2, ' = ', c1**2 + c2**2)