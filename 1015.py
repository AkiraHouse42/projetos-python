n = int(input())

ano = n // 365
resto= n % 365

mes = resto // 30
resto= resto % 30

dia = resto

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')