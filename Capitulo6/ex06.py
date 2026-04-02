pessoas = [
    {'nome': "Iago", 'idade': 65},
    {'nome': "Bryan",'idade': 50},
    {'nome': "Amanda",'idade': 45},
    {'nome': "Manu",'idade':35},
    {'nome': "Igor",'idade':30},
    {'nome': "Vivi",'idade': 25}]

classificacao = sorted(pessoas, key=lambda pessoa: pessoa["idade"], reverse=True)

print(classificacao)