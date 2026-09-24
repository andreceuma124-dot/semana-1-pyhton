segundos_totais = int(input("Digite o tempo em segundos: "))

dias = segundos_totais // 86400
resto_dias = segundos_totais % 86400

horas = resto_dias // 3600
resto_horas = resto_dias % 3600

minutos = resto_horas // 60
segundos = resto_horas % 60

print(
    f"{segundos_totais} segundos equivalem a: {dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)."
)
