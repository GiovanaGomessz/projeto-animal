# from animal import *
# from menu_cao import *

# caes = []
# personas = []


# def criar_cao ():
#     nome = input("Nome do cao: ")
#     tamanho = input("Tamanho do cão: ")
#     raca = input("Qual a raça do cão?: ")
#     idade= input("Idade do cão: ")
#     cor= input("Cor do cão: ")
#     cachorito = Cachorro(nome, tamanho, raca, idade, cor)
#     print(f"Seu cachorro {nome}, está cadastrado! \n")
#     caes.append(cachorito)


# def criar_pessoa ():
#     nome = input("Nome da pessoa: ")
#     idade =input("Qual sua idade?: ")
#     cor=input("Qual sua cor?: ")
#     nacionalidade=input("Qual sua nacionalidade?: ")
#     idioma=input("Qual seu idioma?: ")
#     pessoa = Humano (nome, idade, cor, nacionalidade, idioma)
#     print(f"{nome} você já está cadastrado(a)! \n")
#     personas.append(pessoa)


# while True:
#     op = menu_principal()
#     if op == 1:
#         criar_cao()

#     elif op == 2:
#         criar_pessoa()
    
#     elif op == 3:
#         ver_cao(caes)

#     elif op == 4:
#         ver_humano(personas)

#     elif op == 5:
#         cao_selecionado = None
#         busca = input("Busque pelo seu cachorro: ")
#         caoo = cao_selecionado.buscar_cao(busca)
#         if caoo:
#             print("\nCão encontrado!😉")
#             caoo.mostrar_informacoes()
#             print("\n")
#         else:
#             print("Cão não encontrado😐""\n")


#     elif op == 6:
#         ()

#     elif op == 7:
#         break





# def menu_principal(): 
#     ops = int(input("============= MENU =============\n||  1-Cadastrar Cachorro      ||\n||  2-Cadastrar Humano        ||\n||  3-Listar Cachorros        ||\n||  4-Listar Humanos          ||\n||  5-Buscar cachorro         ||\n||  6-Buscar humano           ||\n||  7-Sair                    ||\n================================\n--> Escolha uma opção: "))
#     return ops

# def ver_cao(lista):
#     for i in lista:
#         print(f"- {i.nome}\n")

# def ver_humano(lista):
#     for i in lista:
#         print(f"- {i.nome}\n")

# def buscar_cao(self, nome):
#     for i in self.caes:
#         if i.nome == nome:
#             return i 
#     else:
#         return False

# def buscar_humano(self, nome):
#     for i in self.personas:
#         if i.nome == nome:
#             return i 
#     else:
#         return False