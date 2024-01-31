A, B, C = input().split(" ")
A, B, C = float(A), float(B), float(C)
pi = 3.14159
TR = (A*C)/2
CI = pi * (C*C)
TRA = (A+B) * (C) /2
Q = (B*B)
R = A * B
print(f'TRIANGULO: {TR:.3f}')
print(f'CIRCULO: {CI:.3f}')
print(f'TRAPEZIO: {TRA:.3f}')
print(f'QUADRADO: {Q:.3f}')
print(f'RETANGULO: {R:.3f}')