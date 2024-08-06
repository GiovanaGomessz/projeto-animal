from animal import *

def criar_cao ():
    nome = input("Nome do cao: ")
    tamanho = input("Tamanho do cão: ")
    raca = input("Qual a raça do cão?: ")
    idade= input("Idade do cão: ")
    cor= input("Cor do cão: ")
    cachorito = Cachorro(nome, tamanho, raca, idade, cor)
    print(f"Seu cachorro {nome}, está cadastrado! \n")
    return cachorito


def criar_pessoa ():
    nome = input("Nome da pessoa: ")
    idade =input("Qual sua idade?: ")
    cor=input("Qual sua cor de pele?: ")
    nacionalidade=input("Qual sua nacionalidade?: ")
    altura=input("Qual sua altura?: ")
    pessoa = Humano (nome, idade, cor, nacionalidade, altura)
    print(f"{nome} você já está cadastrado(a)! \n")
    return pessoa

def listar_cao(lista):
    for i in lista:
        print(f"- {i.nome}\n")

def listar_humano(lista):
    for i in lista:
        print(f"--> {i.nome}\n")


def ver_informacoes_cao(lista):
    for i in lista:
        print(f"⭐ {i.nome}:\n-> {i.tamanho} cm\n-> {i.raca}\n-> {i.idade} anos\n-> {i.cor}\n")        


def ver_informacoes_humano(lista):
    for i in lista:
        print(f"⭐ {i.nome}:\n-> {i.idade} anos\n-> {i.cor}\n-> {i.nacionalidade}\n-> {i.altura}cm\n")


def buscar_cao(caes):
    cao_selecionado = input("Digite o nome do seu cachorro: ")
    for i in caes:
        if cao_selecionado == i.nome:
            print("\nCão encontrado!🐶")
            print(f"⭐ {i.nome}:\n-> {i.tamanho} cm\n-> {i.raca}\n-> {i.idade} anos\n-> {i.cor}\n")
            return i 
      
    else:
        print("Cão não encontrado😿""\n")
        return False
    

def buscar_humano(personas):
    humano_selecionado = input("Digite seu nome: ")
    for i in personas:
        if humano_selecionado == i.nome:
            print("\nPessoa encontrada!🤙 ")
            print(f"⭐ {i.nome}:\n-> {i.idade} anos\n-> {i.cor}\n-> {i.nacionalidade}\n-> {i.altura}cm\n")
            return i 
    else:
        print("Pessoa não encontrada😢")

def jogar_bolinha(caes):
    cao_selecionado = input("Para qual cão vc quer jogar a bolinha? ")
    for i in caes:
        if cao_selecionado == i.nome:
            print(f"\n {i.nome} adorou brincar com a bolinha, ficou muito feliz!!⚾🐶")
            return i 
        
def jogar_graveto(caes):
    cao_selecionado = input("Para qual cão vc quer jogar o graveto? ")
    for i in caes:
        if cao_selecionado == i.nome:
            print(f"\n {i.nome} estava triste😢, mas logo após a brincadeira ficou muito alegre!!😃")
            return i 

def dar_um_osso(caes):
    cao_selecionado = input("Para qual cão vc quer dar um osso? ")
    for i in caes:
        if cao_selecionado == i.nome:
            print(f"\n Como vc adivinhou que {i.nome} estava com fome?!🦴😋")
            return i 
        
def comer(personas):
    pessoa_selecionado = input("Quem esta com fome? ")
    for i in personas:
        if pessoa_selecionado == i.nome:
            print(f"\n Você é vidente? Como adivinhou que {i.nome} estava com fome!😋")
            return i
        
def beber_agua(personas):
    pessoa_selecionado = input("Quem esta com sede? ")
    for i in personas:
        if pessoa_selecionado == i.nome:
            print(f"\n Que água gostosa!{i.nome} realmente estava com sede!🥛")
            return i
        
def ir_ao_banheiro (personas):
    pessoa_selecionado = input("Quem esta apertado(a)? ")
    for i in personas:
        if pessoa_selecionado == i.nome:
            print(f"\nQue bom que {i.nome} tirou a água do joelho!")
 