(This file was created with IA for after improvement of this code so is more like a reference for myself later) 
# QUESTIONÁRIO ESCALA DA MOTIVAÇÃO EM PYTHON

Este programa irá exibir um questionário fraseológico direcionado a estudantes da Educação Básica, com o objetivo de fazer um levantameto de fatores extrínsecos e intrínsecos que afetam a motivação de estudar dos jovens.

Uma breve descrição sobre o que esse projeto faz e para quem ele é

import matplotlib.pyplot as plt

# Lista de perguntas
perguntas = ["Pergunta 1", "Pergunta 2", "Pergunta 3", ..., "Pergunta 31"]

# Dicionário para armazenar as respostas
respostas = {}

# Opções de resposta e pontos correspondentes
opcoes = {"sempre": 3, "talvez": 2, "nunca": 1}

# Contador de pontos
pontos = 0

# Loop através das perguntas
for pergunta in perguntas:
    resposta = ""
    while resposta not in opcoes.keys():
        resposta = input(pergunta + " (sempre/talvez/nunca): ").lower()
        if resposta not in opcoes.keys():
            print("Resposta inválida. Por favor, responda com 'sempre', 'talvez' ou 'nunca'.")
    respostas[pergunta] = resposta
    pontos += opcoes[resposta]

# Imprimir as respostas e a pontuação total
for pergunta, resposta in respostas.items():
    print(f"{pergunta}: {resposta}")
print(f"Pontuação total: {pontos}")

# Criar um gráfico de barras com a pontuação de cada resposta
plt.bar(respostas.keys(), respostas.values())
plt.xlabel('Perguntas')
plt.ylabel('Pontuação')
plt.title('Pontuação por Pergunta')
plt.show()

#acrescentar bd e variação de grafico

import json
import matplotlib.pyplot as plt

# Lista de perguntas
perguntas = ["Pergunta 1", "Pergunta 2", "Pergunta 3", ..., "Pergunta 31"]

# Opções de resposta e pontos correspondentes
opcoes = {"sempre": 3, "talvez": 2, "nunca": 1}

# Contador de pontos
pontos = 0

# Dicionário para armazenar as respostas
respostas = {}

# Loop através das perguntas
for pergunta in perguntas:
    resposta = ""
    while resposta not in opcoes.keys():
        resposta = input(pergunta + " (sempre/talvez/nunca): ").lower()
        if resposta not in opcoes.keys():
            print("Resposta inválida. Por favor, responda com 'sempre', 'talvez' ou 'nunca'.")
    respostas[pergunta] = resposta
    pontos += opcoes[resposta]

# Salvar as respostas no arquivo
with open('respostas.json', 'a') as f:
    json.dump(respostas, f)
    f.write('\n')

# Carregar todas as respostas do arquivo
todas_as_respostas = []
with open('respostas.json', 'r') as f:
    for linha in f:
        todas_as_respostas.append(json.loads(linha))

# Calcular a pontuação total para cada conjunto de respostas
pontuacoes = [sum(opcoes[resposta] for resposta in respostas.values()) for respostas in todas_as_respostas]

# Criar um gráfico de barras com a pontuação de cada conjunto de respostas
plt.hist(pontuacoes, bins=range(min(pontuacoes), max(pontuacoes) + 1))
plt.xlabel('Pontuação')
plt.ylabel('Número de Respostas')
plt.title('Distribuição de Pontuações')
plt.show()


