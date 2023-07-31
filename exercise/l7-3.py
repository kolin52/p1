#Задача 3. Да се създаде програма, която чете думи като вход от клавиатурата, докато
#потребителят не въведе празен ред. След като потребителят въведе празен ред,
#програмата трябва да изведе всяка дума, въведена от потребителя точно веднъж.
#Думите трябва да се показват в същия ред, в който са били въведени.

lines = []
while True:
    l = str(input('Write word: ' ))
    
    if l in lines:
        continue
    
    elif l:
        lines.append(l)
    
    else:
        break;
    
    linestostr = ' '.join([str(l) for l in lines])
print(linestostr)
vert = ''
for word in linestostr:
    vert += word + "\n"
print(vert)
        
        