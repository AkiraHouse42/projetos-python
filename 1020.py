X, Y = input().split(" ")
X, Y = float(X), float(Y)

if (X > 0 and Y > 0):
  print('Q1')
elif(X < 0 and Y > 0):
  print('Q2')
elif(X < 0 and Y < 0):
  print('Q3')
elif(X > 0 and Y < 0):
  print('Q4')
elif(X == 0 and Y != 0):
  print('Eixo Y')
elif(X != 0 and Y == 0):
  print('Eixo X')
else:
  print('Origem')