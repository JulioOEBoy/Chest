from gettext import textdomain

ansi
escape sequence

sempre que for representar uma cor em python

entre [ e m se coloca 3 coisas ou nada o primeir é style segundo text back

style é estilo
text cor do texto
back cor de fundo

\033[m

exemplo \033[0;33;44m

estilos
0 none
1 bold
4 underline sublinhado
7 negative inverter as configurações

texto
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 rosa
36 ciano
37 cinza

de fundo

40 branco
41
42
43
44
45
46
47 cinza

se eu quiser encerrar o back ground só na letra começa ('\033[31;43m Olá mundo!\033[m')
