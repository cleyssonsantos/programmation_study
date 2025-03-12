from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "gourmet")
restaurante_mexicano = Restaurante("Mexican Food", "mexicana")
restaurante_japones = Restaurante("Japa", "japonesa")

restaurante_japones.alternar_estado()
restaurante_japones.receber_avaliacao("Cleysson", 5)
restaurante_japones.receber_avaliacao("Julia", 3)
restaurante_japones.receber_avaliacao("Matheus", 1)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()