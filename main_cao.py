from animal import *
from menu_cao import *

caes = []
personas = []

def criar_cao ():
    nome = input("Nome do cao: ")
    tamanho = input("Tamanho do cão: ")
    raca = input("Qual a raça do cão?: ")
    idade= input("Idade do cão: ")
    cor= input("Cor do cão: ")
    cachorito = Cachorro(nome, tamanho, raca, idade, cor)
    print(f"Seu cachorro {nome}, está cadastrado! \n")
    caes.append(cachorito)


def criar_pessoa ():
    nome = input("Nome da pessoa: ")
    idade =input("Qual sua idade?: ")
    cor=input("Qual sua cor?: ")
    nacionalidade=input("Qual sua nacionalidade?: ")
    idioma=input("Qual seu idioma?: ")
    pessoa = Humano (nome, idade, cor, nacionalidade, idioma)
    print(f"{nome} você já está cadastrado(a)! \n")
    personas.append(pessoa)

def buscar_cao(nome):
    for i in caes:
        if i.nome == nome:
            print("\nCão encontrado!🐶")
            # mostrar_informacoes()
            return i 
    else:
        print("Cão não encontrado😿""\n")
        return False


def buscar_humano(nome):
    for i in personas:
        if i.nome == nome:
            return i 
    else:
        return False

while True:
    op = menu_principal()
    if op == 1:
        while True:
            op_2 = menu_secundario()
            if op_2 == 1:
                criar_cao()
            elif op_2 == 2:
                ver_cao(caes)
            elif op_2 == 3:
                ver_informacoes_cao(caes)
            elif op_2 == 4:
                buscar_cao()
            elif op_2 == 5:
                break

    elif op == 2:
        while True:
            op_3 = menu_terciario()
            if op_3 == 1:
                criar_pessoa()
            elif op_3 == 2:
                ver_humano(personas)
            elif op_3 == 3:
                ver_informacoes_humano(personas)
            elif op_3 == 4:
                break

    elif op == 3:
        break




