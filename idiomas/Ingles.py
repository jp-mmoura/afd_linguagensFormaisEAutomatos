# Ingles.py
from Linguagem import Linguagem

class Ingles(Linguagem):
    def configurar_alfabeto(self):
        return [chr(i) for i in range(ord('a'), ord('z') + 1)]  # Alfabeto a-z
    
    def configurar_transicoes(self):
        return {(estado, simbolo): 'qf' for simbolo in self.configurar_alfabeto() for estado in ['q0', 'qf']}
