def calcular():
    opcao = input('''
Qual das operações abaixo você deseja realizar ?:
+ para adicionar
- para subtrair
* para multiplicar
/ para dividir
''')

    n1 = int(input('Primeiro numero: '))
    n2 = int(input('Segundo numero: '))

    if opcao == '+':
        print('{} + {} = {}'.format(n1, n2, n1+n2))        

    elif opcao == '-':
        print('{} - {} = {}'.format(n1, n2, n1 - n2))        

    elif opcao == '*':
        print('{} * {} = {}'.format(n1, n2, n1 * n2))    

    elif opcao == '/':        
        if n2 == 0:
            print('Você digitou um divisor invalido. Tente novamente!')
        else:
            print('{} / {} = {}'.format(n1, n2, n1 / n2))          

    else:
        print('Você digitou um operador invalido. Tente novamente!')

    reiniciar()

def reiniciar():
    reiniciar_calc = input('''
Você quer reiniciar a calculadora? 
Digite [S] para SIM or [N] for NÃO.
''')

    if reiniciar_calc.upper() == 'S':
        calcular()
    elif reiniciar_calc.upper() == 'N':
        print('Até mais!')
    else:
        reiniciar()
        
calcular()