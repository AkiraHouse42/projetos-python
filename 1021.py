a = input()
b = input()
c = input()

if(a == 'vertebrado' and b == 'ave' and c == 'carnivoro'):
  print('aguia')
elif(a == 'vertebrado' and b == 'ave' and c == 'onivoro'):
  print('pomba')
elif(a == 'vertebrado' and b == 'mamifero' and c == 'onivoro'):
  print('homem')
elif(a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro'):
  print('vaca')
elif(a == 'invertebrado' and b == 'inseto' and c == 'hematofogo'):
  print('pulga')
elif(a == 'invertebrado' and b == 'inseto' and c == 'herbivoro'):
  print('largata')
elif(a == 'invertebrado' and b == 'anelideo' and c == 'hematofogo'):
  print('sanguessuga')
else:
  print('minhoca')