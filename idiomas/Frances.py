# Frances.py
from Linguagem import Linguagem

class Frances(Linguagem):
    def configurar_alfabeto(self):
        return ['a', 'b', 'c', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f', 'g', 'h', 'i', 'î', 'ï', 'j', 'k', 
                'l', 'm', 'n', 'o', 'ô', 'p', 'q', 'r', 's', 't', 'u', 'ù', 'û', 'ü', 'v', 'w', 'x', 'y', 'z']
    
    def configurar_transicoes(self):
        return {(estado, simbolo): 'qf' for simbolo in self.configurar_alfabeto() for estado in ['q0', 'qf']}
