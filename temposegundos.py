segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
segundoentrada = int(segundos_str)

horas = segundoentrada // 3600
segundoresto = segundoentrada % 3600
minutos = segundoresto // 60
segundorestofim = segundoresto % 60
dias = horas // 24

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundorestofim,"segundos.")