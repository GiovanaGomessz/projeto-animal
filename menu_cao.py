def menu_principal(): 
    ops = int(input("\n============= MENU =============\n||  1-Cachorro                ||\n||  2-Humano                  ||\n||  3-Sair                    ||\n================================\nEscolha uma opção: "))
    return ops

def menu_secundario():
    op_2 = int(input("\n=========================\n 1-Cadastrar cachorro\n 2-Listar cachorros\n 3-Ver mais informações\n 4-Buscar cachorro\n 5-Voltar\n=========================\nEscolha uma opção: "))
    return op_2

def menu_terciario():
    op_3 = int(input("\n=========================\n 1-Cadastrar pessoa\n 2-Listar pessoas\n 3-Ver mais informações\n 4-Voltar\n=============================\nEscolha uma opção: "))
    return op_3

def ver_cao(lista):
    for i in lista:
        print(f"- {i.nome}\n")

def ver_informacoes_cao(lista):
    for i in lista:
        print(f"⭐ {i.nome}:\n-> {i.tamanho}\n-> {i.raca}\n-> {i.idade}\n-> {i.cor}")        

def ver_humano(lista):
    for i in lista:
        print(f"--> {i.nome}\n")

def ver_informacoes_humano(lista):
    for i in lista:
        print(f"⭐ {i.nome}:\n-> {i.idade}\n-> {i.cor}\n-> {i.nacionalidade}\n-> {i.idioma}")

