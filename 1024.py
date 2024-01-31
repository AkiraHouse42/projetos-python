hora1, minuto1, hora2, minuto2 = input().split(" ")
hora1, minuto1, hora2, minuto2 = int(hora1), int(minuto1), int(hora2), int(minuto2)

if (hora1 > hora2 or hora1 == hora2 and minuto1 > minuto2 or minuto1 == minuto2):
  hora3 = (hora2 + 24) - hora1
  minuto3 = (minuto2 + 60) - minuto1
  print(f'O JOGO DUROU {hora3} HORA(S) E {minuto3} MINUTO(S)')
else:
  hora4 = hora2 - hora1
  minuto4 = minuto2 - minuto1
  print(f'O JOGO DUROU {hora4} HORA(S) E {minuto4} MINUTO(S)')