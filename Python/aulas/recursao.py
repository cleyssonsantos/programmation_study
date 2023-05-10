# Fatorial sem recursão
"""def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial
    
print(fatorialS(5))"""

# Fatorial - Solução recursiva -> Gera dificuldade para ver problemas, e pode ser ineficiente

def fatorialR(numero):
    if numero == 0: # Critério de 
        return 1
    else:
        # Parâmetro da chamada recursiva
        return numero * (fatorialR(numero - 1))

print(fatorialR(5))
