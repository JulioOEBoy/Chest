num = [2, 5, 9 , 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5) #só elemina o primeiro 2
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')