f = [0,1]

t = int(input())

for i in range(t):
  n = int(input())

  if n == 0:
    print('Fib(0) = 0')
  elif n == 1:
    print('Fib(1) = 1')
  elif n > 1:
    x = 2
    while x <= n:
      f.append(f[x-1] + f[x-2])
      x+=1
    print(f'Fib({n}) = {f[n]}')