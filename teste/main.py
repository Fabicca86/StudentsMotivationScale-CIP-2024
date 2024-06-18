from perguntas import perguntas

nome = (input ('OLÁ, SEJA BEM VINDS! PARA COMEÇAR, QUAL É O SEU NOME? '))       #definir str para input
nome = nome.upper
print(nome, ' VOU TE EXPLICAR COMO FUNCIONA.')
print('''
      AS FRASES A SEGUIR NOS AJUDARÃO A ENTENDER O QUE TE MOTIVA A ESTUDAR.
      RESPONDA COM CALMA POIS NÃO PODERÁ MUDAR A RESPOSTA
      DEPOIS SELECIONE:
        A - PARA SEMPRE
        B - PARA AS VEZES
        C - PARA NUNCA')
      ''')
#código usando listas tuplas e dicionário
#lista de perguntas
#for pergunta in perguntas):
 #   print(pergunta)
#perguntas  = ['pergunta 1', 'pergunta 2','pergunta 3','pergunta 4','pergunta 5','pergunta 6','pergunta 7','pergunta 8','pergunta 9','pergunta 10','pergunta 11','pergunta 12','pergunta 13','pergunta 14','pergunta 15','pergunta 16','pergunta 17','pergunta 18','pergunta 19','pergunta 20','pergunta 21','pergunta 22','pergunta 23','pergunta 24','pergunta 25','pergunta 26','pergunta 27','pergunta 28','pergunta 29','pergunta 30','pergunta 31']
#Dicionário para armazenar as respostas
respostas = { }
#opção de respostas
opcoes = {'SEMPRE', 'AS VEZES', 'NUNCA'}
#contador de pontos
pontos = 0
#LOOP das perguntas
for i , pergunta in enumerate(perguntas): #teste alterando o i
    #definindo pontuação diferente
    if i <18 :
        opcoes = {'SEMPRE':3, 'AS VEZES':2, 'NUNCA':1}
    else:
         opcoes = {'SEMPRE':1, 'AS VEZES':2, 'NUNCA':3}
    resposta = ' '
    while resposta not in opcoes.keys():
        resposta = input(pergunta +' (sempre / as vezes / nunca): ').upper()
        if resposta not in opcoes.keys():
            print('resposta inválida! Por favor responda com SEMPRE, AS VEZES OU NUNCA')
    respostas[pergunta] = resposta
    #Contador dos pontos
    pontos += opcoes[resposta]
#Imprimir as respostas e pontuação total
for pergunta, resposta in respostas.items():
    print (f'{pergunta}: {resposta}')
print (f'Pontuação total: {pontos}')
