# Advent of Code

# Problem 2

def lecture_fichier(fichier):
    """Lis le fichier donné en entrée et renvoie son contenu sous la forme d'un
    tableau de chaines de caracteres. 
    Chaque chaine de caractere est une ligne du fichier passe en argument.
    Renvoie en second le nombre de lignes du fichier."""

    chemin='C:/Users/nicol/OneDrive/Documents/Informatique/advent_of_code/pb_2/'
    F=open(chemin+fichier,'r')

    liste_chaine_caracteres=list()
    for ligne in F:
        liste_chaine_caracteres.append(ligne.split('\n'))

    return tuple((liste_chaine_caracteres, len(liste_chaine_caracteres)))

#print(lecture_fichier("input.txt"))

game1='Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
game2='Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'
game3='Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'
game4='Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'
game5='Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'

def recupere_tirages(game):
    """Renvoie un tableau contenant les differents tirages contenus dans le jeu 'game'
    passe en argument. Ce tableau contient des chaines de caracteres.
    Renvoie egalement le nombre de tirages effectues."""
    nombre_tirages=game.count(';')+1 # nombre de tirages
    indice=game.find(":") # on veut enlever le "Game xx:"
    tirage=game[indice+1:] 
    return tirage.split(";"),nombre_tirages # on recupere les tirages sous la forme d'un tableau de chaines de caracteres

#print(recupere_tirages(game1))
#print(recupere_tirages(game2))
#print(recupere_tirages(game3))
#print(recupere_tirages(game4))
#print(recupere_tirages(game5))

def analyse_tirage(tirage):
    """Renvoie un tableau d'entiers decrivant le nombre de cubes de couleur tires dans le tirage
    donne en argument. Suit le code RGB : donne le nombre de cubes rouges d'abord, puis le nombre
    de cubes verts, et enfin le nombre de cubes bleus.
    Renvoie un tableau de 3 entiers."""

    tableau_resultat = list([0,0,0]) # R,G,B
    indice_resultat=0
    liste_couleurs=['red','green','blue']

    for couleur in liste_couleurs:
        if couleur in tirage:
            indice_couleur=tirage.find(couleur)
            tableau_resultat[indice_resultat]=int(tirage[indice_couleur-3]+tirage[indice_couleur-2])
        indice_resultat+=1
    return tableau_resultat

#print(analyse_tirage(' 3 blue, 4 red'))
#print(analyse_tirage(' 3 green, 15 blue, 14 red'))

def analyse_jeu(game):
    """Renvoie un tableau qui decrit les tirages effectues pour chaque jeu, avec des tableaux RGB.
    Ces tableaux donnent, dans l'ordre, le nombre de cubes rouges, le nombre de cubes verts, 
    le nombre de cubes bleus.
    Renvoie un tableau de tableaux de 3 entiers."""

    liste_tirages=recupere_tirages(game)[0]
    tableau_resultat=list([])

    for tirage in liste_tirages:
        tableau_resultat.append(analyse_tirage(tirage))
    
    return tableau_resultat

#print(analyse_jeu(game1))
#print(analyse_jeu(game2))
#print(analyse_jeu(game3))
#print(analyse_jeu(game4))
#print(analyse_jeu(game5))

def analyse_input(fichier):
    """Renvoie un tableau contenant les nombres de cubes rouges, verts et bleus (dans cet ordre)
    tires pour chaque tirage de chaque jeu, du fichier passe en argument.
    Renvoie un tableau de tableaux de tableaux de 3 entiers."""

    liste_chaine_caracteres,n=lecture_fichier(fichier)[0],lecture_fichier(fichier)[1]
    liste_resultats=list([0]*n)
    indice_resultat=0

    for jeu in liste_chaine_caracteres:
        liste_resultats[indice_resultat]=analyse_jeu(jeu[0])
        indice_resultat+=1

    return liste_resultats

#print(analyse_input('input.txt'))

def traitement_input(fichier):
    """Renvoie un tableau contenant les indices des jeux du fichier passe en argument pour lesquels
    les differents tirages respectent les nombres maximums de cubes fixes par le gnome.
    Renvoie egalement la somme de ce tableau."""

    tableau_input=analyse_input(fichier)
    r_max,g_max,b_max=12,13,14 # nombres maximum de cubes theoriques
    liste_indices_jeux=list([])
    indice_jeu=1

    for jeu in tableau_input:
        flag=True
        for tirage in jeu:
            if tirage[0]>r_max or tirage[1]>g_max or tirage[2]>b_max:
                # on a trouve un tirage qui ne respecte pas les nombres maximum de cubes theoriques, 
                # on ne garde donc pas le jeu associeà ce tirage
                flag=False
        if flag:
            # les tirages du jeu etudie respecte les nombres maximum de cubes theoriques, 
            # on ajoute donc l'indice de ce jeu a notre tableau de resultat
            liste_indices_jeux.append(indice_jeu)
        indice_jeu+=1
    
    return liste_indices_jeux, sum(liste_indices_jeux)

#print(traitement_input('input.txt')) # Resultat : 1734 : OK.
