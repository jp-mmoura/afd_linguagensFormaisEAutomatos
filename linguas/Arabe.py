from Linguagem import Linguagem

class Arabe(Linguagem):
    def configurar_alfabeto(self):
        # Inclui caracteres do alfabeto árabe
        return [chr(i) for i in range(0x0600, 0x06FF + 1)]
