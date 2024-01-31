n = int(input())

Cem = n // 100
resto= n % 100

Cinquenta = resto // 50
resto= resto % 50

Vinte = resto // 20
resto= resto % 20

Dez = resto // 10
resto= resto % 10

Cinco = resto // 5
resto= resto % 5

Dois = resto // 2
resto= resto % 2

Um = resto

print(f'{Cem} nota(s) de R$ 100,00')
print(f'{Cinquenta} nota(s) de R$ 50,00')
print(f'{Vinte} nota(s) de R$ 20,00')
print(f'{Dez} nota(s) de R$ 10,00')
print(f'{Cinco} nota(s) de R$ 5,00')
print(f'{Dois} nota(s) de R$ 2,00')
print(f'{Um} nota(s) de R$ 1,00')