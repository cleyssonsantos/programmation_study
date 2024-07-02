import sys
import os

lista = [
        "284. os.walk para navegar de caminhos de forma recursiva",
        "285. os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)",
        "286. os + shutil - Copiando arquivos e criando pastas com Python",
        "287. os + shutil - Apagando, copiando, movendo e renomeando pastas com Python",
        "288. O que e JSON - JavaScript Object Notation",
        "289. json.dumps e json.loads com strings + typing.TypedDict",
        "290. json.dump e json.load com arquivos",
        "291. Manipulando caminhos, pastas e arquivos no Python com pathlib (aula externa)",
        "292. CSV (Comma Separated Values - Valores separados por virgulas)",
        "293. csv.reader e csv.DictReader para ler arquivos CSV",
        "294. csv.writer e csv.DictWriter para escrever em CSV",
        "295. random tem geradores de numeros pseudoaleatorios (randrange, randint, uniform)",
        "296. random tem geradores de numeros pseudoaleatorios (sample, choices, seed)",
        "297. secrets gera numeros aleatorios seguros",
        "298. string.Template para substituir variaveis em textos",
        "299. (Parte 1) Variaveis de ambiente com os.getenv, os.environ e python-dotenv",
        "300. (Parte 2) Variaveis de ambiente com os.getenv, os.environ e python-dotenv (.env)",
        "301. python-dotenv explicacao simples em texto",
        "302. Configurando o SMTP e senhas de apps no GMAIL para enviar emails com Python",
        "303. Enviando Emails SMTP com Python",
        "304. (Parte 1) ZIP - Compactando Descompactando arquivos com zipfile.ZipFile",
        "305. (Parte 2) ZIP - Compactando Descompactando arquivos com zipfile.ZipFile",
        "306. sys.argv - Executando arquivos com argumentos no sistema",
        "307. argparse.ArgumentParser para argumentos mais complexos",
        "308. (Parte 1) Basico do protocolo HTTP (HyperText Transfer Protocol)",
        "309. (Parte 2) Basico do protocolo HTTP (HyperText Transfer Protocol)",
        "310. http.server - servindo arquivos HTML e CSS via HTTP com um comando Python",
        "311. requests para requisicoes HTTP com Python (entenda request e response)",
        "312. (parte 1) Web Scraping com Python usando requests e bs4 BeautifulSoup",
        "313. (parte 2) Web Scraping com Python usando requests e bs4 BeautifulSoup",
        "314. Adicionando 'encoding' no BeautifulSoup 4 para evitar problemas com caracteres",
        "315. Escolhendo e baixando o chromedriver para o Selenium e Google Chrome",
        "316. Selenium - Automatizando tarefas no navegador",
        "317. Selenium - Selecionando elementos com By, expected_conditions e WebDriverWait",
        "318. Selenium - Enviando teclas com a classe Keys",
        "319. Selenium - find_element e find_elements By",
        "320. TEORIA: subprocess para executando programas e comandos externos",
        "321. subprocess para executando programas e comandos externos",
        "322. Jupyter Notebook - Instalacao e teste",
        "323. Jupyter Notebook - Exemplos",
        "324. (Parte 1) Threads - Executando processamentos em paralelo",
        "325. (Parte 2) Threads - Executando processamentos em paralelo",
        "326. (Parte 3) Threads - Executando processamentos em paralelo",
        "327. PyPDF2 para manipular arquivos PDF (Instalacao)",
        "328. PyPDF2 para manipular arquivos PDF (PdfReader)",
        "329. PyPDF2 para manipular arquivos PDF (PdfWriter)",
        "330. PyPDF2 para manipular arquivos PDF (PdfMerger)",
        "331. Deque - Trabalhando com LIFO e FIFO",
        "332. Dica: remover regras de tipos Unknown do linter do VS Code",
        "333. openpyxl para arquivos Excel xlsx, xlsm, xltx e xltm (instalacao)",
        "334. openpyxl - criando uma planilha do Excel (Workbook e Worksheet)",
        "335. openpyxl - manipulando as planilhas do Workbook",
        "336. openpyxl - ler e alterar dados de uma planilha",
        "337. Pillow: redimensionando imagens com Python",
         ]

def formatar_nome_aula(aula):
    aula = aula.lstrip().replace('.', '', 1).replace(' ', '_')
    aula = aula.replace(':', '_').replace('-', '_')
    return f"aula{aula}.py"

diretorio_atual = os.path.dirname(sys.argv[0])

for aula in lista:
    nome_arquivo = formatar_nome_aula(aula)
    
    caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)
    
    with open(caminho_arquivo, 'w') as f:
        f.write(f"#Arquivo {nome_arquivo} criado com sucesso.\n")
    
    print(f"Arquivo {nome_arquivo} criado no diretório: {diretorio_atual}")
