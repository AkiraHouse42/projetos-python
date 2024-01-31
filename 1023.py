tempo1, tempo2 = input().split()
tempo1, tempo2 = int(tempo1), int(tempo2)

if (tempo1 > tempo2 or tempo1 == tempo2):
  hora = (tempo2 + 24) - tempo1
  print(f'O JOGO DUROU {hora} HORA(S)')
else:
  hora2 = tempo2 - tempo1
  print(f'O JOGO DUROU {hora2} HORA(S)')