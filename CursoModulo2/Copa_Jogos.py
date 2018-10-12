import requests

print('\033[1;34m-=-' * 20, '\n        Fifa Word Cup 2018\n\nJogos e Resultados \n      \n', '-=-' * 20)
print('\033[1;32m')
jogos=requests.get('http://worldcup.sfg.io/matches').json()
for jogo in jogos:
    if jogo['status']in('completed','in progress'):
        print(jogo['home_team']['country'],
              jogo['home_team']['goals'],'x',
              jogo['away_team']['goals'],
              jogo['away_team']['country'])