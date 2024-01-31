a = []

for i in range(4):
  a.append(float(input()))
for i in range(4):
  if a[i] <= 10:
    print(f'A[{i}] = {a[i]:.1f}')