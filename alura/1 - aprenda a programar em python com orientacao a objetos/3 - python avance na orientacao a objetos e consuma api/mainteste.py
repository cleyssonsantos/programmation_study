import requests
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url=url)
print(response)

if response.status_code == 200:
    dados_json = response.json()

    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item["Company"]

        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]
        })


else:
    print(f"O erro foi {response.status_code}")


# for nome_do_restaurante, dados in dados_restaurante.items():
#     nome_do_arquivo = f"{nome_do_restaurante}.json"
#     with open(nome_do_arquivo, "w") as arquivo_restaurante:
#         json.dump(dados, arquivo_restaurante, indent=4)



# Sobre a cotação atual:

link_cotacao = "https://economia.awesomeapi.com.br/last/USD-BRL"

response = requests.get(link_cotacao)
response_json = response.json()
cotacao_atual = float(response_json["USDBRL"]["bid"])
mensagem = f"O dólar está custando R$ {cotacao_atual:.2f}"
print(mensagem)

