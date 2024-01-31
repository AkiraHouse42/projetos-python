for i in range(1,10):
  for j in range(1,4):
    if i%2 != 0:
      j = 8 - j
      print(f'I={i} J={j}')