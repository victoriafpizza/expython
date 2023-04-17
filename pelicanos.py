somatoria = 0
asas = 1 
while asas != 0 :
    print("digite um comprimento de asa")
    print("pressione 0 para encerrar")
    asas = float(input())
    somatoria += asas
print(f"somatoria das asas {somatoria}")