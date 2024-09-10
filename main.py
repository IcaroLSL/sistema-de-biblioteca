# Variáveis
dadosDosLivros = {}  # Dicionário que guarda os livros cadastrados. A chave é o ISBN e o valor é uma lista com título, autor e ano.
empréstimos = {}  # Dicionário que guarda os empréstimos de livros. A chave é o ISBN e o valor é um dicionário com usuário e data do empréstimo.

# Módulos
from time import sleep  # Importa a função 'sleep' para fazer pausas no código
import datetime  # Importa o módulo para lidar com datas e horas
import os  # Importa o módulo para manipular arquivos e diretórios


# Funções

def cadastrar_livros():
    """
    Cadastra um novo livro no sistema.
    Pede as informações do livro para o usuário (título, autor, ano e ISBN) e adiciona esses dados ao dicionário
    'dadosDosLivros', usando o ISBN como chave.
    """
    print("##### Cadastrar Livro ##### ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    anoDePublicacao = int(input("Ano de Publicação: "))
    isbn = input("Código ISBN: ")
    listaDadosLivro = [titulo, autor, anoDePublicacao]
    dadosDosLivros[isbn] = listaDadosLivro
    print("Livro cadastrado com sucesso!")
    sleep(0.5)


def consultar_livros():
    """
    Mostra todos os livros que estão cadastrados no sistema.
    Exibe o ISBN, título, autor e ano de publicação de cada livro no dicionário 'dadosDosLivros'.
    """
    print("##### Consulta Livros #####")
    for isbn, dados in dadosDosLivros.items():
        print(f"ISBN: {isbn}, Título: {dados[0]}, Autor: {dados[1]}, Ano de Publicação: {dados[2]}")
    print("Livros consultados com sucesso!")
    sleep(1)


def registrar_emprestimo():
    """
    Registra um empréstimo de livro.
    Pede o ISBN do livro e o nome do usuário que está fazendo o empréstimo, e salva essas informações no dicionário
    'empréstimos'. A data do empréstimo é registrada automaticamente.
    """
    print("##### Registrar Empréstimo #####")
    isbn = input("ISBN do Livro: ")
    nomeDoUsuario = input("Nome do Usuário: ")
    dataEmpréstimo = datetime.datetime.now()
    empréstimos[isbn] = {'usuario': nomeDoUsuario, 'data_emprestimo': dataEmpréstimo}
    print("Empréstimo registrado com sucesso!")
    sleep(0.5)


def relatório_emprestimos():
    """
    Gera um relatório dos livros que estão emprestados.
    Exibe uma tabela com o título do livro, o nome do usuário e a data do empréstimo para cada empréstimo registrado.
    """
    print("##### Relatório de Livros Emprestados #####")
    print("Título" + " " * 40 + "Usuário" + " " * 40 + "Data do Empréstimo")
    print("=" * 111)
    for isbn in empréstimos:
        titulo = dadosDosLivros[isbn][0]
        nomeDoUsuario = empréstimos[isbn]['usuario']
        dataEmpréstimo = empréstimos[isbn]['data_emprestimo'].strftime('%d/%m/%Y')
        print(titulo + " " * 40 + nomeDoUsuario + " " * 40 + dataEmpréstimo)
    print("Relatório de empréstimos gerado com sucesso!")
    sleep(0.5)


def salvar_dados():
    """
    Salva os dados dos livros e dos empréstimos em arquivos de texto.
    Primeiro, verifica se os arquivos 'livros.txt' e 'emprestimos.txt' existem. Se não existirem, eles são criados.
    Em seguida, escreve os dados dos livros e dos empréstimos nos arquivos respectivos.
    """
    # Verifica e cria o arquivo de livros se não existir
    if not os.path.exists('livros.txt'):
        with open('livros.txt', 'w') as arquivoLivros:
            pass  # Cria o arquivo vazio se não existir

    # Salva os dados dos livros
    with open('livros.txt', 'w') as arquivoLivros:
        for isbn in dadosDosLivros:
            titulo = dadosDosLivros[isbn][0]
            autor = dadosDosLivros[isbn][1]
            anoDePublicacao = dadosDosLivros[isbn][2]
            arquivoLivros.write(f"{isbn},{titulo},{autor},{anoDePublicacao}\n")

    # Verifica e cria o arquivo de empréstimos se não existir
    if not os.path.exists('emprestimos.txt'):
        with open('emprestimos.txt', 'w') as arquivoEmpréstimos:
            pass  # Cria o arquivo vazio se não existir

    # Salva os dados dos empréstimos
    with open('emprestimos.txt', 'w') as arquivoEmpréstimos:
        for isbn in empréstimos:
            nomeDoUsuario = empréstimos[isbn]['usuario']
            dataEmpréstimo = empréstimos[isbn]['data_emprestimo'].strftime('%d/%m/%Y %H:%M:%S')
            arquivoEmpréstimos.write(f"{isbn},{nomeDoUsuario},{dataEmpréstimo}\n")

    print("Dados salvos com sucesso!")


def carregar_dados():
    """
    Carrega os dados dos livros e dos empréstimos a partir dos arquivos de texto.
    Verifica se os arquivos 'livros.txt' e 'emprestimos.txt' existem e cria-os se não existirem.
    Lê os dados dos arquivos e os coloca nos dicionários 'dadosDosLivros' e 'empréstimos'.
    """
    global dadosDosLivros, empréstimos

    # Verifica e cria o arquivo de livros se não existir
    if not os.path.exists('livros.txt'):
        with open('livros.txt', 'w') as arquivoLivros:
            pass  # Cria o arquivo vazio se não existir
    else:
        with open('livros.txt', 'r') as arquivoLivros:
            for linha in arquivoLivros:
                partes = linha.strip().split(',')
                isbn = partes[0]
                titulo = partes[1]
                autor = partes[2]
                ano = int(partes[3])
                dadosDosLivros[isbn] = [titulo, autor, ano]
        print("Dados dos livros carregados com sucesso!")

    # Verifica e cria o arquivo de empréstimos se não existir
    if not os.path.exists('emprestimos.txt'):
        with open('emprestimos.txt', 'w') as arquivoEmpréstimos:
            pass  # Cria o arquivo vazio se não existir
    else:
        with open('emprestimos.txt', 'r') as arquivoEmpréstimos:
            for linha in arquivoEmpréstimos:
                partes = linha.strip().split(',')
                isbn = partes[0]
                usuario = partes[1]
                data_emprestimo = datetime.datetime.strptime(partes[2], '%d/%m/%Y %H:%M:%S')
                empréstimos[isbn] = {'usuario': usuario, 'data_emprestimo': data_emprestimo}
        print("Dados dos empréstimos carregados com sucesso!")

    sleep(0.25)


def calcular_tempo_emprestimo():
    """
    Calcula o tempo restante para devolver um livro emprestado.
    Pede o ISBN do livro e calcula quantos dias faltam para a devolução, considerando um prazo de 14 dias.
    """
    isbn = input("Digite o ISBN do livro para consultar o tempo de empréstimo: ")
    data_emprestimo = empréstimos[isbn]['data_emprestimo']
    prazo_devolucao = data_emprestimo + datetime.timedelta(days=14)
    dias_restantes = (prazo_devolucao - datetime.datetime.now()).days
    print(f"{dias_restantes} dias")
    sleep(0.5)


# Código principal
carregar_dados()  # Carrega os dados dos arquivos quando o programa começa

while True:
    print("Bem-vindo ao Sistema de Gerenciamento de Biblioteca!")
    print("1. Cadastrar Livro")
    print("2. Consultar Livros")
    print("3. Registrar Empréstimo")
    print("4. Relatório de Livros Emprestados")
    print("5. Consulta Tempo Empréstimo")
    print("6. Sair")
    opção = input("Escolha uma opção: ")

    if opção == "1":
        sleep(0.5)
        cadastrar_livros()
    elif opção == "2":
        sleep(0.5)
        consultar_livros()
    elif opção == "3":
        sleep(0.5)
        registrar_emprestimo()
    elif opção == "4":
        sleep(0.5)
        relatório_emprestimos()
    elif opção == "5":
        sleep(0.5)
        calcular_tempo_emprestimo()
    elif opção == "6":
        salvar_dados()  # Salva todos os dados antes de fechar o programa
        print("Fechando o programa")
        break
    else:
        print("Opção não identificada, escolha uma opção válida!")
        sleep(1.5)
