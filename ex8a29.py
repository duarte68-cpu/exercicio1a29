# # exercicio 1
# numero1 = int(input('digite um numero inteiro: '))
# numero2 = int(input('digite segundo numero inteiro: '))
# soma = numero1 + numero2
# print(f'A soma entre {numero1} e {numero2} O resultado da soma {soma}\n')

# #exercicio 2
# sub1 = int(input('digite um numero inteiro: '))
# sub2 = int(input('digite a segundo numero inteiro: '))
# resultado = sub1 - sub2
# print(f'A sulbtração do {sub2} e {sub1} o resultado é {resultado}\n' )

# # exercicio 3
# mult1 = int(input('digite um numero interiro: '))
# mult2 = int(input('digite segundo numero inteiro: '))
# multi = mult1 * mult2
# print(f'A soma entre {mult1} e {mult2} resultado {multi}\n')

# # exercicio 4
# div1 = int(input('digite um numero inteiro'))
# div2 = int(input('digite segundo numero'))
# divisão = div1 / div2
# print(f'A soma entre {div2} e {div1} O resultado {divisão}')

# # exercicio 5
# numero1 = int(input('digite um numero inteiro: '))
# numero2 = int(input('dugite segundo numero: '))
# resultado = numero1%numero2
# print('O resto da divisão ', resultado)

# # exercicio 6
# numero1 = int(input('digite um numero inteiro: '))
# expoente = int(input('digite expoente numero: '))
# potencia = numero1**expoente
# print(f'A potencia entre {numero1} e {numero2} e {potencia}')

# # exercicio 7 media de três numeros
# numero1 = int(input('digite um numero: '))
# numero2 = int(input('digite segundo numero: '))
# numero3 = int(input('digite segundo numero: '))
# media = (numero1+numero2+numero3)/3
# print(f'A media entre {numero1} numero {numero2} numero {numero3} resultado {media:.2}')

# exercicio 8
#temperatura = float(input('informe temperatuda: '))
#resultado = temperatura*1.8+32
#print(f'A temperatura em farenaite {resultado} Fahrenheit\n')

# exercicio 9
#reais = float(input('digite um valor em reais: '))
#dolar = reais / 5.50
#print(f'Valor em reais {reais} convertido em {dolar}')

# exercicio 10
#altura = float(input('informe a altura do retangulo: '))
#largura = float(input('informe a largura do triangulo: '))
#area = largura*altura
#print(f'O total da area e {area}')

# exercicio 11
#perimetro = float(input('digite um lado do quadrado: '))
#soma = perimetro*2
#print('O perimetro de um quadrado e: ', soma)

# exercicio 12
#base = float(input('insira a base: '))
#altura = float(input('insira a altura: '))
#area = (base + altura) / 2
#print('O resultado da base da area é', base,'\n')

# exercicio 13
#raio = float(input('insira o raio: '))
#pi = float(3.14159)
#resultado = pi * (raio**2)
#print('O resultado da area do circulo é ',resultado)

# exercicio 14
#metro = float(input('insira a quntidade de metros: '))
#centimetro = metro * 100
#print('O metro convertido em centimetros é ', centimetro, 'centimetros')

# exercicio 15
#horas = float(input('insira quantidade de horas trabalhadas: '))
#valor = float(input('insira o valor por hora: '))
#salario = horas * valor
#print('o valor do salario é', salario)

# exercicio 16
#preco = float(input('insira o valor do produto: '))
#porcentual = float(input('digite o desconto: '))
#desconto = (preco*porcentual)/100
#print(f'O desconto do produto é {desconto} %')

# exercicio 17
#distancia = float(input('insira distancia percorrida: '))
#tempo_percorrido = float(input('insira o tempo percorrido: '))
#velocidade_media = distancia / tempo_percorrido
#print(f'a velocidade media percorrido é {velocidade_media} kmh')

# exercicio 18
#idade = int(input('digite idade: '))
#resultado = idade * 365
#print(f'Sua idade em dias é {resultado}')

# exercicio 19
#segundos = int(input('digite dia: '))
#dia = 24 * 3600
#print(f'A guantidade de segundo em um dia é {dia} segundos')

# exercicio 20
#peso = float(input('insira seu peso: '))
#altura = float(input('insira sua altura: '))
#imc = peso/(altura*altura)
#print(f'Seu indice de massa corporal é {imc}')

# exercicio 21
#numero_primeiro = int(input('insira um numero: '))
#numero_segundo = int(input('insira segundo numero: '))
#resultado = numero_primeiro//numero_segundo
#print(f'A diferenca entre numero é:{resultado}')

# exercicio 22
#numero1 = int(input('digite um numero inteiro: '))
#numero2 = int(input('digite segundo numero inteiro: '))
#resultado = numero1 / numero2
#print(f'O numero inteiro de {numero1} e numero {numero2} é: {int(resultado)}')

# exercicio 23
#numero = int(input('insira um numero inteiro: '))
#absoluto = abs(numero)
#print(f'o valor absoluto é: {numero}')

# exercicio 24
#velocidade = int(input('informe a velocidade em km: '))
#velocidade_ms = velocidade / 3.6
#print(f'o ms e: {velocidade_ms: .5f} metros por segundos')

# exercicio 25
#numero_a = float(input('digite um valor a: '))
#numero_b = float(input('digite um valor b: '))
#numero_c = float(input('digite um valor c: '))

#delta = (numero_b ** 2) - 4 * numero_a * numero_b
#print('\n')
#resultado1 = (- numero_b + delta ** (1 / 2)) / (2 * numero_a)
#resultado2 = (- numero_b + delta ** (1 / 2)) / (2 * numero_a)

#print('O resultado é: ',resultado1)
#print('O resultaso é: ',resultado2)

# exercicio 26
#preco1 = float(input('valor do produto R$: '))
#preco2 = float(input('valor segundo produto R$: '))
#preco3 = float(input('valor terçeiro produto R$: '))
#total = preco1 + preco2 + preco3
#print(f'O valor total a pagar: {total}')

# exercicio 27
#dia = int(input('insida dias da semana: '))
#semanas = dia // 7
#dias_restantes = dia % 7
#print(f'dia da semana {semanas} e dias {dias_restantes}')

# exercicio 28
# produto = float(input('digite um valor R$: '))
# desconto_5 = (5 * produto)/100
# desconto_10 = (10 * produto)/100
# resultado1 = produto - desconto_10
# resultado2 = produto - desconto_5
# if resultado1 > 500:
#   print(f'o produto com desconto é: {resultado1}')
  
# elif resultado1 < 500:
#   print(f'o produto com descoto é: {resultado2}')
  
# # exercicio 29
# numero1 = float(input('digite um numero: '))
# numero2 = float(input('digite o segundo numero: '))
# print(f'resultado da divisão é: {numero1 / numero2}')
