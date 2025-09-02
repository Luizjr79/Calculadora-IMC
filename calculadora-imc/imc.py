print ('Vamos calcular seu IMC?')
# Mensagem de Apresentação

peso = float (input('Digite seu peso: '))
# Pedir o peso

altura = float (input('Digite sua altura: '))
# Pedir a altura

imc = (peso / (altura ** 2))

print (f"Seu peso é {peso}Kg e sua altura é {altura}m")
# Mensagem de confirmação

print (f"Seu IMC é {imc:.1f}")

# Valores de acordo com a OMS
if imc < 18.5:
    print ('CLASSIFICAÇÃO: ABAIXO DO PESO')

elif 18.5 <= imc <= 24.9:
    print ('CLASSIFICAÇÃO: PESO NORMAL')

elif 25.0 <= imc <= 29.9:
    print ('CLASSIFICAÇÃO: SOBREPESO')

elif 30.0 <= imc <= 34.9:
    print ('CLASSIFICAÇÃO: OBESIDADE GRAU I')   

elif 35.0 <= imc <= 39.9:
    print ('CLASSIFICAÇÃO: OBESIDADE GRAU II')

else:
    print ('CLASSIFICAÇÃO: OBESIDADE GRAU III(MÓRBIDA)')