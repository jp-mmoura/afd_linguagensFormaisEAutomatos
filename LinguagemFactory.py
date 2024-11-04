from Familias import Familia
from linguas.Latino import Latino
from linguas.Cirilico import Cirilico
from linguas.Arabe import Arabe
from linguas.Grego import Grego
from linguas.CJK import CJK
from linguas.Assembly import Assembly
from linguas.Java import Java
from linguas.JavaScript import JavaScript
from linguas.Python import Python


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
        elif idioma == Familia.ASSEMBLY:
            return Assembly()
        elif idioma == Familia.JAVA:
            return Java()
        elif idioma == Familia.JAVASCRIPT:
            return JavaScript()
        elif idioma == Familia.PYTHON:
            return Python()
        else:
            raise ValueError("Idioma não suportado.")
