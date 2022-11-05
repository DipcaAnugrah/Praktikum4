print('Dipca Anugrah')
print(312210666)
print(':)')

a = []
b = int (input('Masukkan bilangan: '))
while b != 0:
    b = int (input('Masukkan bilangan: '))
    if a == 0:
        break
    a.append(b)
print('Bilangan terbesar adalah: ',max(a))