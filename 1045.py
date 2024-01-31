T = []

T = int(input())
V = 0
for i in range(1000):
  print(f'N[{i}] = {V}')
  V+=1
  if(V==T):
    V=0