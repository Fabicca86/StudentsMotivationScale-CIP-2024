from perguntas import perguntas

nome = (input ('OLÁ, SEJA BEM VINDS! PARA COMEÇAR, QUAL É O SEU NOME? '))       #personalization of test with user name
nome = nome.upper
print(nome, ' VOU TE EXPLICAR COMO FUNCIONA.') #first simple orientations
print('''
      AS FRASES A SEGUIR NOS AJUDARÃO A ENTENDER O QUE TE MOTIVA A ESTUDAR.
      RESPONDA COM CALMA POIS NÃO PODERÁ MUDAR A RESPOSTA
      DEPOIS SELECIONE:
        A - PARA SEMPRE
        B - PARA AS VEZES
        C - PARA NUNCA')
      ''')
#código usando listas, loops e dicionário

#Dicionário para armazenar as respostas
respostas = { }
#opção de respostas
opcoes = {'SEMPRE', 'AS VEZES', 'NUNCA'}
#contador de pontos
pontos = 0
#LOOP for the questions
for i , pergunta in enumerate(perguntas): # iteract with questions because they have diferent values from 1 to 17 and 18 to 31
    #definindo pontuação diferente
    if i <18 :
        opcoes = {'SEMPRE':3, 'AS VEZES':2, 'NUNCA':1}
    else:
         opcoes = {'SEMPRE':1, 'AS VEZES':2, 'NUNCA':3}
    resposta = ' '
    while resposta not in opcoes.keys(): # loop condition for case the user don't respond well
        resposta = input(pergunta +' (sempre / as vezes / nunca): ').upper()
        if resposta not in opcoes.keys():
            print('resposta inválida! Por favor responda com SEMPRE, AS VEZES OU NUNCA')
    respostas[pergunta] = resposta    #saving the answers
    #Contador dos pontos
    pontos += opcoes[resposta]
#Imprimir as respostas e pontuação total
for pergunta, resposta in respostas.items(): #show options to user
    print (f'{pergunta}: {resposta}')
print (f'Pontuação total: {pontos}') #this should not be messaged for user, so after when improving the code to do a graph i will remove it, just to see if count is OK
