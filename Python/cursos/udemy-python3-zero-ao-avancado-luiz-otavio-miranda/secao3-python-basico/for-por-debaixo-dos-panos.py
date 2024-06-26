# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador

texto = "Cleysson"
iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
