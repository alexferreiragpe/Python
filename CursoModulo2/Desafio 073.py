print(80*'\033[35m-=-')
titulo='Brasileirão 2018'
print(titulo.center(150))
times=('Internacional','São Paulo','Palmeiras','Flamengo','Atlético-MG','Grêmio','Cruzeiro','Santos','Fluminense','Corinthians','América-MG','Vitória','Bahia','Atlético-PR','Botafogo','Vasco','Sport','Ceará','Chapecoense','Paraná')
print(80*'-=-')
print('\033[36mLista de times do Brasileirão:',times)
print(80*'-=-')
print('\033[33mOs 5 primeiros colocados na tabela:',times[0:5])
print(80*'-=-')
print('\033[34mOs 4 últimos colocados são: ',times[-4:])
print(80*'-=-')
print('\033[35mTimes em Ordem Alfabética: ',sorted(times))
print(80*'-=-')
for p,time in enumerate(times):
    if(times[p]=='Chapecoense'):
        print('\033[32mO time Chapecoense está na {}ª posição'.format(p+1))