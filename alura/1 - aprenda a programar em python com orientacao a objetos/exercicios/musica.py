class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    
    def __str__(self):
        return f"Nome da música: {self.nome} | Artista/Banda: {self.artista} | Duração: {self.duracao} segundos"

musica_um = Musica('Reverie', 'Polyphia', 400)
print(musica_um)