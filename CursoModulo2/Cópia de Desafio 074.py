import random
valor=[]
valor=random.sample(range(1,600),5)
print('\n\033[95mValores Gerados aleatoriamente: ',valor)
print('\n\033[94mO Maior valor Gerado foi o {}'.format(max(valor)))
print('\033[93mO Menor valor Gerado foi o {}'.format(min(valor)))