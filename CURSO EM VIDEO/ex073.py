times = ('internacional', 'corinthians', 'ceará', 'fortaleza', 'botafogo', 'flamengo', 'palmeiras',
         'juventude', 'fluminense', 'grêmio', 'vasco da gama', 'cruzeiro', 'bahia', 'são paulo',
         'red bull bragantino', 'santos', 'atlético mineiro', 'atlético goianiense', 'cuiabá', 'coritiba')

print(f'Lista de times do Brasileirão: {times}')
print(f'Os 5 primeiros times{(times[:5])}')
print(f'Os 4 últimos 4 colocados{times[-4:]}')
print(f'Times em ordem alfabetica{sorted(times)}')
print(f'Em que posição está vasco da gama: {times.index("vasco da gama") + 1}º lugar')
