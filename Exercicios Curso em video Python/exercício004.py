teste = input('Insira a variável que você quer testar:')
print('A variável é numérica?',teste.isnumeric())
print('A variável é alfanumérica?', teste.isalnum())
print('A variável é alfa?', teste.isalpha())
print('A variável é somente maiúscula?', teste.isupper())
print('Avariável é apenas minúscula?', teste.islower())
print('A variável é capitalizada (primeira maiúscula e o restante minúscula?', teste.istitle())