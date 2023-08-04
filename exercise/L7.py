# Задача 5. За да спечели най-голямата награда в определена лотария, човек трябва да
# съпостави всичките 6 числа от билета си с 6-те числа между 1 и 49, които са изтеглени от
# организатора на лотарията. Напишете програма, която генерира произволен избор от 6
# числа за лотариен билет. Уверете се, че избраните 6 числа не се повтарят. Покажете
# числата във възходящ ред

import random

ticket = []

for numb in range(6):
    numb = random.randint(1,49)
    if numb not in ticket:
        ticket.append(numb)
    elif numb in ticket:
        numb = random.randint(1,49)
        ticket.append(numb)
        
ticket.sort()
tickettostr = ' '.join([str(numb) for numb in ticket])
print(tickettostr)
    
