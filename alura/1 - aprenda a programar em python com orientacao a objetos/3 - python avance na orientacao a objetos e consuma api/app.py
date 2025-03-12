from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

# restaurante_praca = Restaurante("praça", "gourmet")
# restaurante_mexicano = Restaurante("Mexican Food", "mexicana")
restaurante_japones = Restaurante("Japa", "japonesa")
bebida_suco = Bebida("Morango ao Leite", 13.0, "Grande")
prazo_sushi = Prato("Sushi de Salmão", 3.0, "O melhor sushi da região")
sobremesa_pudim = Sobremesa("Pudim de Chocolate", 15.0, "Grande")

restaurante_japones.adicionar_no_cardapio(bebida_suco)
restaurante_japones.adicionar_no_cardapio(prazo_sushi)
restaurante_japones.adicionar_no_cardapio(sobremesa_pudim)

bebida_suco.aplicar_desconto()
prazo_sushi.aplicar_desconto()
sobremesa_pudim.aplicar_desconto()

# restaurante_japones.alternar_estado()
# restaurante_japones.receber_avaliacao("Cleysson", 5)
# restaurante_japones.receber_avaliacao("Julia", 3)
# restaurante_japones.receber_avaliacao("Matheus", 1)

def main():
    # Restaurante.listar_restaurantes()
    # print(bebida_suco)
    # print(prazo_sushi)
    restaurante_japones.exibir_cardapio

if __name__ == "__main__":
    main()
