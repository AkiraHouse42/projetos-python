vetor = []

for i in range(10):
  vetor.append(int(input()))
for i in range(10):
  if vetor[i] <= 0:
    vetor[i] = 1
    print(f'X[{i}] = {vetor[i]}')
  else:
    print(f'X[{i}] = {vetor[i]}')