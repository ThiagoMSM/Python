import random
import textwrap
def constroiMsg(ingles):
    if ingles:
        return {
            "msgInicial": textwrap.dedent("""
            +=======================================+
           '     | Welcome to my game, muggle!           |
                | Enter an integer number               |
                | and guess what number I've            |
                | picked for you.                       |
                | So, what is the secret number?        |
                +=======================================+
                """),
                "tentativaFalha": "Ha, ha! You're stuck in my loop!",
                "msgPedirNum": "Enter a number: ",
                #"msgPedirNumInc'rementada": "Try to read my mind, enter the number I'm thinking of: ",
            "acertou": "Well done, muggle! You are free now",
            "excecao": "Please enter only valid integers"
        }
    else:
        return {
            "msgInicial": textwrap.dedent("""
            +=======================================+
            | Bem vindo ao meu jogo, trouxa!        |
            | Insira um número inteiro              |
            | E adivinhe qual número eu             |
            | escolhi pra você.                     |
            | Então, qual é o número secreto?       |
            +=======================================+
            """),
            "tentativaFalha": "Ha, ha! Você está preso em meu looping",
            "msgPedirNum": "Insira um número: ",
            #"msgPedirNumIncrementada": "Tente ler a minha mente, informe o número que estou pensando: ",
            "acertou": "Bem feito, trouxa! Você está livre agora",
            "excecao": "Por favor, insira só números inteiros"
        }
    
def Main():
    numSecreto = random.randrange(1,10)
    #numSecreto = 777
    lang = input(textwrap.dedent("""
        Would you like to play the game in english? Y/N
        Deseja jogar o jogo em inglês? Y/N """))
    
    while lang.upper() not in ["Y","N"]:
        print(textwrap.dedent("""
            ----ERROR! Please, enter only Y (yes), or N, (no)----
            ----ERRO! Por favor, informe apenas Y (sim), ou N, (não)----"""))
        
        lang = input(textwrap.dedent("""
            Would you like to play the game in english? Y/N
            Deseja jogar o jogo em inglês? Y/N """))
        
    msgs = constroiMsg(lang.upper() == "Y") # N == Y ---> true, false
    print(msgs['msgInicial'])

    while True:
        try:
            numEscolhido = int(input(msgs['msgPedirNum']))
        except:
            print(msgs['excecao'])
            continue 

        if (numEscolhido != numSecreto):
            print(msgs['tentativaFalha'])
            continue
        else:
            print(msgs['acertou'])
            break
            
Main()