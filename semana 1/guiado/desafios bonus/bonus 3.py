frase = input("Digite uma frase: ").strip()

numero_caracteres = len(frase)
numero_palavras = len(frase.split())
frase_maiuscula = frase.upper()

print(
    f"Análise da frase:\n"
    f"• Nº de caracteres: {numero_caracteres}\n"
    f"• Nº de palavras: {numero_palavras}\n"
    f"• Em maiúsculas: {frase_maiuscula}"
)
