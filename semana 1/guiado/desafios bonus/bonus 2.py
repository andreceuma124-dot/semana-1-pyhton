import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * (raio**2)
circunferencia = 2 * math.pi * raio

print(
    f"Para um círculo de raio {raio:.2f}:\n"
    f"• Área: {area:.2f}\n"
    f"• Circunferência: {circunferencia:.2f}"
)
