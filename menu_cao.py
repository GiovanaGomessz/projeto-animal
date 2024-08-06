def menu_principal(): 
    ops = int(input("\n============= MENU =============\n||  1-Cachorro                ||\n||  2-Humano                  ||\n||  3-Sair                    ||\n================================\nEscolha uma opção: "))
    return ops

def menu_secundario():
    op_2 = int(input("\n=============== SUBMENU ================\n 1-Cadastrar cachorro\n 2-Listar cachorros\n 3-Ver mais informações\n 4-Buscar cachorro\n 5-Brincar com cão\n 6-Voltar\n=======================================\nEscolha uma opção: "))
    return op_2

def menu_terciario():
    op_3 = int(input("\n=============== SUBMENU ================\n 1-Cadastrar pessoa\n 2-Listar pessoas\n 3-Ver mais informações\n 4-Buscar pessoa\n 5- Ações\n 6-Voltar\n===================================\nEscolha uma opção: "))
    return op_3

def menu_brincar():
    op_b = int(input("\n============= Brincadeiras =============\n 1-Jogar bolinha\n 2-Jogar graveto\n 3- Dar um osso\n 4-Voltar\n=======================================\nEscolha uma opção:  "))
    return op_b

def menu_acoes():
    op_a = int(input("\n============= AÇÕES =============\n 1- Comer\n 2- Beber Água\n 3- Ir ao banheiro\n 4-Voltar\n==============================\nEscolha uma opção: "))
    return op_a