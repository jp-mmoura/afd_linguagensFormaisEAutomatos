from Linguagem import Linguagem

class Cirilico(Linguagem):
    def configurar_alfabeto(self):
        # Inclui caracteres do alfabeto cirílico
        return [chr(i) for i in range(0x0400, 0x04FF + 1)]
