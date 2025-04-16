print('Coloque aqui o primeiro termo!')
p = int(input('--'))
print('Coloque aqui a razão!')
r = int(input('--'))
for c in range(1, 11):
    print(f'a({c}) = {p} + ({c} - 1) × {r} = {p + (c - 1) * r}')
