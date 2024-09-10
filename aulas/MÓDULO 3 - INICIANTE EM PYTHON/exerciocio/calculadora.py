try:
    while True:
        n1 = int(input('Informe um número '))
        n2 = int(input('Informe outro número '))
        operadores_permitidos = '+-*/**'
        operacao = input('Informe a operação que deseja realizar(*, /, +, -, **): ')
        if operacao == '*':
            print(n1 * n2)
        elif operacao == '+':
            print(n1 + n2)
        elif operacao == '-':
            print(n1 - n2)
        elif operacao == '/':
            print(float(n1 / n2))
        elif operacao == '**':
            print(n1 ** n2)
        if operacao not in operadores_permitidos: #Verifica se tem na variável e oda se tiver
            print('Operação Inválida')
            continue # continue joga pra cima quando não tem os operadores
        sair = input('Deseja [S]air? ').lower().startswith('s')   
        if sair is True: 
            break
except:
    print('Error')