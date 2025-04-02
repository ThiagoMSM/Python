clas1 = input()
clas2 = input()
clas3 = input()

if clas1 == "vertebrado":
    if clas2 == "ave":
        if clas3 == "carnivoro":
            print("aguia")
        elif clas3 == "onivoro":
            print("pomba")
    elif clas2 == "mamifero":
        if clas3 == "onivoro":
            print("homem")
        elif clas3 == "herbivoro":
            print("vaca")

elif clas1 == "invertebrado":
    if clas2 == "inseto":
        if clas3 == "hematofago":
            print("pulga")
        elif clas3 == "herbivoro":
            print("lagarta")
    elif clas2 == "anelideo":
        if clas3 == "hematofago":
            print("sanguessuga")
        elif clas3 == "onivoro":
            print("minhoca")

"""
# outra alternativa:
# milhões de vezes melhor de entender c/ dicionários... mas, não foi visto em sala, por isso fiz e comentei, mas fica aqui de lembrete que esta versão é preferível!!
classes = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero":{
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },

    "invertebrado":{
        "inseto":{
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo":{
            "hematofago":"sanguessuga",
            "onivoro":"minhoca"
        }
    }
}

print(classes[clas1][clas2][clas3])"""