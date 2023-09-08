import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, aqui vai sua receita!!\n\nIngredientes:\n\n2 colheres (sopa) de manteiga sem sal.\n2 colheres (sopa) de farinha de trigo.\n1 xícara (chá) de leite em temperatura ambiente (200 ml).\n2 sachês de Tempero ao seu gosto.\n2 pitadas de sal.\n1 caixinha de creme de leite (200 g).\nmeia xícara (chá) de água (100 ml).\n1 xícara (chá) de ervilhas congeladas (90 g).\n1 xícara (chá) de brócolis em floretes pequenos, cozidos "al dente" (80 g).\nMeia xícara (chá) queijo tipo parmesão ralado (100 g).\n1 pacote de macarrão tipo talharim, cozido "al dente" (500 g)\n\nModo de preparo:\n1- Em uma panela pequena, coloque a manteiga e leve ao fogo alto para derreter. Junte a farinha de trigo e mexa sem parar, por meio minuto, sem deixar dourar.\n2- Aos poucos, acrescente metade do leite, mexendo sem parar, e cozinhe por 1 minuto ou até ficar homogêneo e espesso. Adicione o Tempero, o sal, o creme de leite, o leite restante, a água, a ervilha, o brócoli e o queijo ralado, e cozinhe por mais 2 minutos, mexendo sempre, ou até aquecer.\n3- Retire do fogo, regue o macarrão e sirva em seguida.\n\nReceita pronta! Bom apetite! :){os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, aqui vai sua receita para 10 porções!!\n\nIngredientes:\n\n3 peitos de frango cortados em cubos.\nSal a gosto\n1 cebola picada\n1 colher (sopa) de manteiga\n1/3 copo (americano) de mostarda\n1 copo(americano) de creme de leite.\n1 dente de alho picado.\nPimenta do reino a gosto.\n2 colheres (sopa) de maionese.\n1/2 copo (americano).\n1 copo (americano) de cogumentos (opcional).\nBatata palha a gosto.\n\nModo de preparo:\n1- Em uma panela, misture o frango, o alho, a maionese, o sal e a pimenta.\n2- Em uma frigideira grande, derreta a manteiga e doure a cebola.\n3- Junte o frango temperado até que esteja dourado.\n4- Adicione o cogumelo (opcional), o ketchup e a mostarda.\n5- Incorpore o creme de leite e retire do fogo antes de ferver.\n6- Sirva com arroz branco e batata palha.\n\nReceita pronta! Bom apetite! :){os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, aqui vai sua receita para 4 porções!!\n\nIngredientes:\n\n500g de coxão mole (cortados em cubo).\n2 dentes de alho picados.\n1 cebola média picada.\n1 pitada de pimenta do reino.\n2 batatas médias cortadas em cubos ou de acordo com a sua preferência.\n200g de molho de tomate.\nCheiro verde, salsinha (quanto preferir).\n1 caldo de carne.\n2 colheres de sopa de óleo.\n2 folhas de louro (opcional).\n1 colher de chá de orégano (opcional).\n1 cenoura pequena cortada em rodelas.\n 500ml de água em temperatura ambiente.\n\nModo de preparo:\n1- Em uma panela funda, coloque o óleo e os cubos de carne e deixe fritar (vai soltar bastnate água).\n2- Quando começar a secar, coloque a cebola, o alho, orégano, pimenta-do-reino, caldo de carne, as folhas de louro e deixe refogar (OBS: Atenção para não deixar a carne queimar).\n3- Depois acrescente 250ml de água e deixe cozinhar por 5 minutos.\n4- Coloque as batatas, a cenoura, o cheiro verde picado, cebolinha e o restante da água.\n5- Deixe cozinhar por 30 mnutos e por fim coloque o molho de tomate e mexa bem, deixando por mais 5 minutos no fogo.\n\nReceita pronta! Bom apetite! :){os.linesep}')    
    else:
        print('Escolha uma das opções: 1, 2 ou 3')    


def start():
    #Apresentar o chatbot
    print('Olá, eu sou o Bino, seu ajudante chefe! Seja bem-vindo ao meu chat')

    #Pedir o nome
    nome = input('Como posso te chamar? ')
    
    while True:

        #Oferecer um menu de opções
        resposta = input(
            f'{os.linesep}{nome}, o que deseja cozinhar hoje? {os.linesep}[1] - Macarrão ao molho branco com brócolis e ervilha {os.linesep}[2] - Strogonoff de frango {os.linesep}[3] - Picadinho de carne com batata e cenoura{os.linesep}')
        
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ =='__main__':
    start()