from abc import ABC, abstractmethod

class Linguagem(ABC):
    def __init__(self):
        self.alfabeto = self.configurar_alfabeto()
    
    @abstractmethod
    def configurar_alfabeto(self):
        """Define o alfabeto da família de idiomas."""
        pass

    def calcular_pontuacao(self, palavra):
        """Verifica se todos os caracteres da palavra estão exclusivamente no alfabeto."""
        palavra_filtrada = ''.join(letra.lower() for letra in palavra if letra.isalpha())  # Ignora espaços e símbolos, usa minúsculas
        if all(letra in self.alfabeto for letra in palavra_filtrada):  # Todos os caracteres devem estar no alfabeto
            return len(palavra_filtrada)  # Retorna uma pontuação proporcional ao comprimento da palavra
        return 0  # Retorna 0 se algum caractere não estiver no alfabeto
