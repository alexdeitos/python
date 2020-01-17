exp = str(input('Digite a expressão: ')).strip().lower()
aberto = fechado = 0
for letter in exp:
    if letter == '(':
       aberto += 1
    elif letter == ')':
       fechado += 1
if aberto != fechado:
   print('Sua expressão é inválida!')
else:
   print('Sua expressão é válida!')

'''
exp.count('(')
exp.count(')')
'''
