salario = float(input())

if (salario >= 0 and salario <= 2000):
  print('Isento')
elif (salario >= 2000 and salario <= 3000):
  conta = (salario - 2000.00) * 0.08
  print(f'R$ {conta:.2f}')
elif (salario >= 3000 and salario <= 4500):
  conta2 = (salario - 3000) * 0.18 + (1000*0.08)
  print(f'R$ {conta2:.2f}')
else:
  conta3 = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
  print(f'R$ {conta3:.2f}')