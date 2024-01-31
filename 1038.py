x = int(input())
a = 0
b = 1

for i in range(x):
  if i == x - 1:
    print(a)
  else:
    print(a, end = " ")

    c = b+a
    a = b
    b = c