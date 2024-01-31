par = []
impar = []

for i in range(15):
  vetor = int(input())

  if vetor % 2 == 0:
    par.append(vetor)
  elif vetor % 2 != 0:
    impar.append(vetor)

for i in range(5):
  if len(par) == 5:
    print(par)
    par = []
  elif len(impar) == 5:
    print(impar)
    impar = []

print(f'par[{len(par)}] = {par}')
print(f'impar[{len(impar)}] = {impar}')