segundos_totais = int(input("Digite o tempo em segundos: "))

horas = segundos_totais // 3600
resto = segundos_totais % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas}h {minutos}m {segundos}s")
