a, b, c = input().split(' ')
a, b, c = float(a), float(b), float(c)

delta = b - 4 *a*c
x1= ((-b + delta ** (1/2))/2)
x2= ((-b - delta ** (1/2))/2)

if(a==0 and delta <0):
  print('Impossivel calcular')
else:
  print(f'R1 = {x1:.5f}')
  print(f'R2 = {x2:.5f}')