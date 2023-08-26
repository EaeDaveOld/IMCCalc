# Calculadora de IMC

print("### CALCULADORA DE IMC ###")  # Mostra ao usuário a proposta do programa

while True:  # Criando um laço de repetição
    try:  # Tratamento de erros com try
        altura = float(input('Digite sua altura (em metros) - ( e use "." no lugar da ","): '))
        peso = float(input('Digite o seu peso (em kg) - (e use "." no lugar da ","): '))

        imc = peso / (altura ** 2)
        print(f'Você tem {altura}m de altura, {peso}kg de peso e seu IMC é de: {imc:.2f}')

        if imc < 18.5:
            print('Seu estado de classificação é "Magreza"')
        elif imc >= 18.5 and imc < 25:
            print('Seu estado de classificação é "Normal"')
        elif imc >= 25 and imc < 30:
            print('Seu estado de classificação é "Sobrepeso"')
        elif imc >= 30 and imc < 35:
            print('Seu estado de classificação é "Obesidade grau I"')
        elif imc >= 35 and imc < 40:
            print('Seu estado de classificação é "Obesidade grau II"')
        elif imc > 40:
            print('Seu estado de classificação é "Obesidade grau III"')

        novo_calculo = input('Deseja fazer um novo cálculo de IMC? [S]im ou [N]ão: ').lower().startswith('s')
        if novo_calculo is True:
            continue
        else:
            break

    except ValueError:  # Se ocorrer algum tipo de erro de valor, então vai exibir as seguintes opções:
        print('O valor digitado é inválido, digite somente números e utilize "." ao invés de ","')
        tentar_novamente = input('Deseja tentar novamente? [S]im ou [N]ão: ').lower().startswith('s')
        if tentar_novamente is True:
            continue
        else:
            break
