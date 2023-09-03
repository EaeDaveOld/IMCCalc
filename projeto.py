print("### CALCULADORA DE IMC ###")

while True:
    try:
        altura = float(input('Digite sua altura (em metros, use "." no lugar da ","): '))
        peso = float(input('Digite o seu peso (em kg, use "." no lugar da ","): '))

        if altura <= 0 or peso <= 0:
            print('Altura e peso devem ser valores positivos e maiores que zero.')
            continue

        imc = round(peso / (altura ** 2), 1)

        print(f'Você tem {altura}m de altura, {peso}kg de peso e seu IMC é de: {imc}')

        if imc < 18.5:
            print('Seu estado de classificação é "Magreza".')
        elif imc < 24.9:
            print('Seu estado de classificação é "Normal".')
        elif imc < 29.9:
            print('Seu estado de classificação é "Sobrepeso".')
        elif imc < 34.9:
            print('Seu estado de classificação é "Obesidade grau I".')
        elif imc < 39.9:
            print('Seu estado de classificação é "Obesidade grau II".')
        else:
            print('Seu estado de classificação é "Obesidade grau III".')

        novo_calculo = input('Deseja fazer um novo cálculo de IMC? [S]im ou [N]ão: ').lower().startswith('s')
        if not novo_calculo:
            break

    except ValueError:
        print('O valor digitado é inválido, digite somente números e utilize "." ao invés de ",".')
        tentar_novamente = input('Deseja tentar novamente? [S]im ou [N]ão: ').lower().startswith('s')
        if not tentar_novamente:
            break
