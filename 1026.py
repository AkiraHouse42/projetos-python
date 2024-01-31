pedido, quantidade = input().split(' ')
pedido, quantidade = int(pedido), int(quantidade)

if (pedido == 1):
  preco = 4 * quantidade
  print(f'Total: R$ {preco:.2f}')
elif (pedido == 2):
  preco = 4.50 * quantidade
  print(f'Total: R$ {preco:.2f}')
elif (pedido == 3):
  preco = 5 * quantidade
  print(f'Total: R$ {preco:.2f}')
elif (pedido == 4):
  preco = 2 * quantidade
  print(f'Total: R$ {preco:.2f}')
else:
  preco = 1.50 * quantidade
  print(f'Total: R$ {preco:.2f}')