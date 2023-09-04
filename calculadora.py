#print('Calculadora')

#def calculadora():
#    operacao = input()
#print('Digite dois numeros:')

#n1 = int(input())
#n2 = int(input())
#operacao = (input())

#print('Digite a operacao:')
#if operacao == '+':
#    print(f"A soma de {n1} + {n2}")
#    print(n1 = n2)

print('calculadora')

print('n1:')
n1 = int(input())

print('op: (+, -, *, /)')
op = input()

print('n2:')
n2 = int(input())

#print(f"Resultado: {n1+n2}")

if op == '+':
    print(f'Resultado: {n1 + n2}')

elif op == '-':
    print(f'Resultado: {n1 - n2}')

elif op == '*':
    print(f'Resultado: {n1 * n2}')

elif op == '/':
    print(f'Resultado: {n1/n2}')

else: 
    print('Operacao invalida')