from abc import ABC, abstractmethod

class Linguagem(ABC):
    def __init__(self):
        self.estados = ['q0', 'qf']  # Estado inicial e estado final
        self.estado_inicial = 'q0'
        self.estados_finais = ['qf']
        self.alfabeto = self.configurar_alfabeto()
        self.transicoes = self.configurar_transicoes()

    @abstractmethod
    def configurar_alfabeto(self):
        """Define o alfabeto específico da linguagem."""
        pass

    def configurar_transicoes(self):
        """Define as transições para cada símbolo no alfabeto, permitindo transições de qualquer estado."""
        transicoes = {}
        for simbolo in self.alfabeto:
            for estado in self.estados:
                transicoes[(estado, simbolo)] = 'qf'
        return transicoes

    def processar_palavra(self, palavra):
        """Processa a palavra/frase verificando se todos os caracteres estão no alfabeto da linguagem, ignorando espaços."""
        for simbolo in palavra:
            if simbolo == " ":  # Ignorar espaços em branco
                continue
            if simbolo not in self.alfabeto:
                print(f"Caractere '{simbolo}' não encontrado no alfabeto da linguagem {self.__class__.__name__}.")
                return False
        print(f"A palavra/frase '{palavra}' foi reconhecida na linguagem {self.__class__.__name__}.")
        return True
