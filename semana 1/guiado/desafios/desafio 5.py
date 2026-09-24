preco = float(input("Preço original (R$): "))
desconto = float(input("Percentual de desconto (%): "))

preco_final = preco - (preco * (desconto / 100))

print(f"Preço com desconto: R$ {preco_final:.2f}")
