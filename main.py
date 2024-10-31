from LinguagemFactory import LinguagemFactory
from Idiomas import Idioma

# Configurando o autômato para o idioma escolhido
def configurar_linguagem(idioma_escolhido):
    return LinguagemFactory.get_linguagem(idioma_escolhido)

# Função para processar a cadeia e identificar o idioma
def processar_cadeia(linguagem, cadeia):
    estado_atual = linguagem.estado_inicial
    for simbolo in cadeia:
        if (estado_atual, simbolo) in linguagem.transicoes:
            estado_atual = linguagem.transicoes[(estado_atual, simbolo)]
        else:
            return None  # Não reconhecido
    return estado_atual in linguagem.estados_finais  # Retorna True se aceito

# Teste com uma entrada
palavra = "gracias"
idiomas = [Idioma.ESPANHOL, Idioma.INGLES, Idioma.FRANCES, Idioma.PORTUGUES]
reconhecido = False

for idioma in idiomas:
    linguagem = configurar_linguagem(idioma)
    if processar_cadeia(linguagem, palavra):
        print(f"A palavra '{palavra}' foi reconhecida como pertencente ao idioma: {idioma.value}.")
        reconhecido = True
        break

if not reconhecido:
    print(f"A palavra '{palavra}' não foi reconhecida por nenhum idioma.")

