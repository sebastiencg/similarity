import spacy
import requests

url = "https://trouve-mot.fr/api/random"

model = spacy.load('en_core_web_lg')


def jeu():
    i = 0
    response = requests.get(url).json()
    mot_secret = response[0]["name"]
    while i < 2:
        jeton_mot_secret = model(mot_secret)
        mot_donne = input("Entrez votre mot  indice : " + response[0]["categorie"] + " ")
        if mot_donne == "aide moi":
            print(response[0]["name"])
            i += 1
        jeton_mot_donne = model(mot_donne)

        similarite = jeton_mot_donne.similarity(jeton_mot_secret)

        if similarite == 1.0:
            print('Félicitations ! Vous avez gagné ;)!')
            i += 1
        else:
            message = "Le mot '" + jeton_mot_donne.text + "' est similaire à " + str(
                similarite * 100) + "% au mot secret."
            print(message)



def start_game_function():
    choix = input("lancer le jeu oui/non ")

    if choix == "oui":
        jeu()
    elif choix == "non":
        print(' a la prochaine bg')
    else:
        print('pas compris')
        start_game_function()


start_game_function()
response = requests.get(url).json()
mot_secret = response[0]["name"]
