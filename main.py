from LinguagemFactory import LinguagemFactory
from Familias import Familia

# Configurando o autômato para a família de escrita escolhida
def configurar_linguagem(familia_escolhida):
    return LinguagemFactory.get_linguagem(familia_escolhida)

# Input da palavra
palavra = input("Digite uma palavra para identificar a família de escrita: ").strip()
familias = [Familia.LATINO, Familia.CIRILICO, Familia.ARABE, Familia.GREGO, Familia.CJK]
resultados = {}

# Calcula a pontuação de cada família de escrita para a palavra inserida
for familia in familias:
    linguagem = configurar_linguagem(familia)
    pontuacao = linguagem.calcular_pontuacao(palavra)
    resultados[familia.value] = pontuacao

# Identificar a família de escrita com a maior pontuação
familia_reconhecida = max(resultados, key=resultados.get)

print(f"A palavra '{palavra}' foi identificada como pertencente à família de escrita: {familia_reconhecida}.")
