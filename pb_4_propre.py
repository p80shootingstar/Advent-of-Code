# Advent of Code

# Problem 4

def lecture_fichier(fichier):
    """Lis le fichier donné en entrée et renvoie son contenu sous la forme d'un
    tableau de chaines de caracteres. 
    Chaque chaine de caractere est une ligne du fichier passe en argument.
    Renvoie en second le nombre de lignes du fichier."""

    chemin='C:/Users/nicol/OneDrive/Documents/Informatique/advent_of_code/pb_4/'
    F=open(chemin+fichier,'r')

    liste_chaine_caracteres=list()
    for ligne in F:
        liste_chaine_caracteres.append(ligne.split())

    F.close()

    return tuple((liste_chaine_caracteres, len(liste_chaine_caracteres)))

############################################## Donnees test ###########################################################################################################################

card1='Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
card2='Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'
card3='Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'
card4='Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'
card5='Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'
card6='Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'

#######################################################################################################################################################################################

def playing_card(card):
    """Renvoie le score de la carte passee en argument.
    Compare les numeros gagnants avec les numeros joues.
    Si le nombre de numeros joues trouves parmi les numeros gagnants est inferieur ou egal a 1,
    le score de la carte est ce nombre.
    Si ce nombre de numeros joues parmi les numeros gagnants est superieur strictement a 1, 
    le score de la carte vaut 2**(ce nombre-1)."""

    border_card=card.index("|") # repereage de l'indice auquel apparait le sperateur | entre les winning numbers et les nombres que l'on a.
    nb_characters=len(card)
    counter=0 # nombre de numeros joues parmi les numeros gagnants

    list_winning_number=list([0]*(border_card-2))
    # le -2 sert a ne pas tenir compte des deux premieres chaines de caracteres qui sont de la forme 'card' + 'n°:'
    for k in range(border_card-2):
        list_winning_number[k]=card[2+k]

    list_playing_number=list([0]*(nb_characters-border_card-1))
    for k in range(nb_characters-border_card-1):
        list_playing_number[k]=card[border_card+k+1]

    for x in list_winning_number:
        if x in list_playing_number:
            #print(x)
            counter+=1

    if counter<=1:
        return counter
    return 2**(counter-1)

#print(playing_card(card1.split())) # 8 points : OK
#print(playing_card(card2.split())) # 2 points : OK
#print(playing_card(card3.split())) # 2 points : OK
#print(playing_card(card4.split())) # 1 point : OK
#print(playing_card(card5.split())) # 0 point : OK
#print(playing_card(card6.split())) # 0 point : OK

def solve(fichier):
    """Renvoie la somme des scores de chaque carte contenue dans le fichier passe en argument."""

    list_cards=lecture_fichier(fichier)[0]
    solution=0

    for card in list_cards:
        solution+=(playing_card(card))

    return solution

#print(solve("input.txt")) # 24 160 : bonne reponse, OK.