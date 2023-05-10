# insert -> recebe o index da lista e o valor que quer inserir
# append -> coloca o que quer adicionar, mas só recebe 1 valor, se quiser uma lista tem que adicionar [], porém vai ser inserido
# na lista uma lista dentro da lista, o que as vezes não é o que queremos

# extend -> é o mesmo que o append praticamente, mas quando por [] ele vai adicionar cada elemento separado dentro de uma unica lista
# o que a maioria das vezes é o que queremos

lista = ['Ola', 'mundo', 'jorge']
lista.extend(['Mais', 'Itens', 'Na', 'Lista'])

print(lista)
