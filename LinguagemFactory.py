# LinguagemFactory.py
from Idiomas import Idioma
from idiomas.Espanhol import Espanhol
from idiomas.Ingles import Ingles
from idiomas.Frances import Frances
from idiomas.Portugues import Portugues

class LinguagemFactory:
    @staticmethod
    def get_linguagem(idioma: Idioma):
        if idioma == Idioma.ESPANHOL:
            return Espanhol()
        elif idioma == Idioma.INGLES:
            return Ingles()
        elif idioma == Idioma.FRANCES:
            return Frances()
        elif idioma == Idioma.PORTUGUES:
            return Portugues()
        else:
            raise ValueError("Idioma não suportado.")
