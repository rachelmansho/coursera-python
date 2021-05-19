segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
segundo_entrada = int(segundos_str)


horas = segundo_entrada // 3600
segundo_resto = segundo_entrada % 3600
minutos = segundo_resto // 60
segundo_restofim = segundo_resto % 60
dias = horas // 24
horas_fim = horas % 24

print(dias,"dias,",horas_fim,"horas,",minutos,"minutos e",segundo_restofim,"segundos.")
