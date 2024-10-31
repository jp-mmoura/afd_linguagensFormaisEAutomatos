from Familias import Familia
from linguas.Latino import Latino
from linguas.Cirilico import Cirilico
from linguas.Arabe import Arabe
from linguas.Grego import Grego
from linguas.CJK import CJK

class LinguagemFactory:
    @staticmethod
    def get_linguagem(idioma: Familia):
        if idioma == Familia.LATINO:
            return Latino()
        elif idioma == Familia.CIRILICO:
            return Cirilico()
        elif idioma == Familia.ARABE:
            return Arabe()
        elif idioma == Familia.GREGO:
            return Grego()
        elif idioma == Familia.CJK:
            return CJK()
        else:
            raise ValueError("Idioma não suportado.")
