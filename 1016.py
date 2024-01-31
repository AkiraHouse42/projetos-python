n = float(input())

Cem = n // 100
resto = n % 100

Cinquenta = resto // 50
resto = resto % 50

Vinte = resto // 20
resto = resto % 20

Dez = resto // 10
resto = resto % 10

Cinco = resto // 5
resto = resto % 5

Dois = resto // 2
resto = resto % 2

um = resto // 1
resto = resto % 1

cinquentaCents = resto // 0.50
resto = resto % 0.50

vinteCinco = resto // 0.25
resto = resto % 0.25

dezcents = resto // 0.10
resto = resto % 0.10

cincocents = resto // 0.05
resto = resto % 0.05

umcents = resto // 0.01

print('NOTAS:')
print(f'{Cem:.0f} nota(s) de R$ 100.00')
print(f'{Cinquenta:.0f} nota(s) de R$ 50.00')
print(f'{Vinte:.0f} nota(s) de R$ 20.00')
print(f'{Dez:.0f} nota(s) de R$ 10.00')
print(f'{Cinco:.0f} nota(s) de R$ 5.00')
print(f'{Dois:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{um:.0f} moeda(s) de R$ 1.00')
print(f'{cinquentaCents:.0f} moeda(s) de R$ 0.50')
print(f'{vinteCinco:.0f} moeda(s) de R$ 0.25')
print(f'{dezcents:.0f} moeda(s) de R$ 0.10')
print(f'{cincocents:.0f} moeda(s) de R$ 0.05')
print(f'{umcents:.0f} moeda(s) de R$ 0.01')