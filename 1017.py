a, b, c, d = input().split(' ')
a, b, c, d = int(a), int(b), int(c), int(d)

e = a + b
f = c + d

if(b > c and d > a and f > e and c > 0 and d > 0 and a % 2 == 0):
  print('Valores aceitos')
else:
    print('Valores nao aceitos')