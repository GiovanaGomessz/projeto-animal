class Animal: 
    nome: str
    coracao: bool
    racional: bool
    idade: int
    tipo: str
    cor: str

    def __init__ (self, nome, coracao, racional, idade, cor, tipo):
            self.nome=nome
            self.coracao=coracao
            self.racional=racional
            self.idade=idade
            self.cor=cor
            self.tipo=tipo

    
class Humano(Animal):
    nome= ''
    idade = 0
    cor = ''
    nacionalidade= ''
    idioma= ''
    personas = []

    def __init__ (self, nome, idade, cor, nacionalidade, idioma):
        self.nome=nome
        self.idade= idade
        self.cor=cor
        self.nacionalidade=nacionalidade
        self.idioma=idioma
        self.coracao = True
        self.racional=True
 
    def pessoa(self):
        print(self.nome)
        print(self.idade)
        print(self.raca)
        print(self.nacionalidade)
        print(self.idioma)


class Cachorro(Animal):
    nome = ''
    tamanho = 0
    raca = ''
    idade = 0
    cor = ''
    caes = []

    def __init__ (self,nome,tamanho, raca, idade, cor):
    
        self.nome = nome
        self.tamanho = tamanho
        self.raca = raca
        self.idade = idade
        self.cor = cor
        self.coracao = True
        self.racional = False

    def cao (self):
        print(self.nome )
        print(self.tamanho )
        print(self.raca)
        print(self.idade )
        print(self.cor)


    



