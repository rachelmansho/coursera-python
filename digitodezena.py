numero_entrada = input("Digite um número inteiro: ")
numero = int(numero_entrada)

valor = numero // 10
resto = valor % 10

print("O dígito das dezenas é", resto)
