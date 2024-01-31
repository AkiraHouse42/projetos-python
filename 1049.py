m = int(input())
p = input().split(' ')

for i in range(m):
  p[i] = int(p[i])

  menor = p[0]
  posicao = 0

for i in range(m):
  if (p[i] < menor):
    menor = p[i]
    posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')