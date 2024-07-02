import os

caminho = os.path.join("/home", "kronus", "Desktop", "Exemplo")
print(caminho)

for pasta in os.listdir(caminho):
    # Checar se é realmente uma pasta
    if os.path.isdir(pasta):
        print(pasta)
    
    # Pra checar o conteúdo dentro das pastas, tem que criar um novo caminho
    caminho_completo_pasta = os.path.join(caminho, pasta)

    for imagem in os.listdir(caminho_completo_pasta):
        print("    ", imagem)
