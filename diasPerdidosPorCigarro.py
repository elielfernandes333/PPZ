cigarrosPorDia = int(input("Quantos cigarros você fuma por dia? "))
anosFumando = int(input("Há quantos anos você fuma? "))

cigarrosFumados = anosFumando * 365 * cigarrosPorDia
diasPerdidos = cigarrosFumados * 10 / 1440

print(f"Você perdeu {diasPerdidos:.2f} dias de vida até agora.")
