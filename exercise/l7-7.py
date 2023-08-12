#Задача 7. Напишете програма, която намира максимална редица от последователни
#еднакви елементи в списък.
#Пример: {2, 1, 1, 2, 3, 3, 2, 2, 2, 1} -> {2, 2, 2}. ‘2’ * counter

#Algoritm
# Create empty list
# Find equal digits
# Create lists with equal digits
# Len lists and compare lists


a = [2,1,1,2,3,3,2,2,2,1]
b = []
i = 0
while i < len(a) - 1:
    nested=[]
    while a[i]==a[i + 1]:
        nested.append(a[i])
        i += 1
    nested.append(a[i])
    b.append(nested)
    i += 1
    
print(b)

longest = b[0] if b else None
for x in b:
    if len(x) > len(longest):
        longest = x
print(longest)

#Second
a = [2,1,1,2,3,3,2,2,2,1]
b = []
i = 0
while i < len(a) - 1:
    b = []
    consec = []
    while a[i] == a[i + 1]:
        consec.append(a[i])
        i += 1
    consec.append(a[i])
    b.append(consec)
    i += 1
    if len(consec) > len(b):
        b = consec
print(consec)





