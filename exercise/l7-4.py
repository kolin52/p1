#Задача 4. Да се създаде програма, която да чете цели числа въведени от потребителя,
#докато не бъде въведен празен ред. След като всичките числа са прочетени, програмата
#трябва да показва всички отрицателни числа, последвани от нули, последвани от всички
#положителни числа. Във всяка група номерата трябва да се показват в същия ред, в
#който са въведени от потребителя. Например, ако потребителят въведе стойностите 3,
# -4, 1, 0, -1, 0 и -2, вашата програма трябва да изведе стойностите -4, -1, -2, 0, 0, 3 и 1 .
# Вашата програма трябва да показва всяка стойност на нов ред.

#Numbers of digits

n = int(input('insert digit - numbers of digit in list: '))

l1 = []
l2 = []
l3 = []
for numb in range(n):
    numb = int(input('insert digit: '))
    if numb < 0:
        l1.append(numb)
    elif numb ==  0:
        l2.append(numb)
    elif numb > 0:
        l3.append(numb)
    else:
        raise Exception ('String Length is Not Equal')
    
print(l1)
print(l2)
print(l3)
print(*(l1 + l2 + l3))