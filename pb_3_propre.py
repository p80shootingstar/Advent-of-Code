# Advent of Code

# Problem 3

def lecture_fichier(fichier):
    """Lis le fichier donné en entrée et renvoie son contenu sous la forme d'un
    tableau de chaines de caracteres. 
    Chaque chaine de caractere est une ligne du fichier passe en argument.
    Renvoie en second le nombre de lignes du fichier."""

    chemin='C:/Users/nicol/OneDrive/Documents/Informatique/advent_of_code/pb_3/'
    F=open(chemin+fichier,'r')

    liste_chaine_caracteres=list()
    for ligne in F:
        liste_chaine_caracteres.append(ligne.split('\n'))

    F.close()

    return tuple((liste_chaine_caracteres, len(liste_chaine_caracteres)))

############################################## Donnees test ###########################################################################################################################

ligne0=['1234567890']
ligne1=['467..114..']
ligne2=['...*......']
ligne3=['..35..633.']
ligne4=['......#...']
ligne5=['617*......']
ligne6=['.....+.58.']
ligne7=['..592.....']
ligne8=['......755.']
ligne9=['...$.*....']
ligne10=['.664.598..']

ligne11=['12.......*..']
ligne12=['+.........34']
ligne13=['.......-12..']
ligne14=['..78........']
ligne15=['..*....60...']
ligne16=['78.........9']       
ligne17=['15.....23..$']
ligne18=['8...90*12...']
ligne19=['............']
ligne20=['2.2......12.']
ligne21=['.*.........*']
ligne22=['1.1..503+.56']

test_2=[ligne11,ligne12,ligne13,ligne14,ligne15,ligne16,ligne17,ligne18,ligne19,ligne20,ligne21,ligne22]

######################################################################################################################################################################################

def new_analyse_matrice(lign_table):
    """Renvoie la somme des nombres contenus dans la matrice passee en argument qui presentent la propriete suivante : 
    ces nombres sont entoures d'un caractere special.
    En argument : un tableau de tableaux de chaines de caracteres, vu comme une matrice.
    Le nombre de sous-tableaux = nombre de lignes de la matrice.
    Le nombre de caracteres d'une chaine de caractere d'un sous-tableau = nombre de colonnes."""

    # Dimensions de la matrice
    lign_number=len(lign_table)
    column_number=len(lign_table[0][0])
    # On parcourt la matrice ligne par ligne, donc sous-tableau par sous-tableau.
    index_lign=0

    # Tableau de resultats intermediaires : il contient des chaines de caracteres des nombres qui verifient la propriete souhaitee.
    intermediate_results=list([])

    print(lign_table)

    for lign in lign_table:

        index_begin=0 # parcours caractere par caractere

        while index_begin<len(lign[0]): # condition d'arret : on ne sort pas d'un sous-tableau.
            # VARIANT DE BOUCLE : index_begin strictement croissant.
            index_end=0

            while index_begin+index_end<len(lign[0]) and lign[0][index_begin+index_end].isdigit(): # recuperation des sequences de digits dans le sous-tableau.
                # VARIANT DE BOUCLE : index_end strictement croissant.
                index_end+=1

            if index_end!=0: # verification pour la sequence de digits retenue, de la presence de caracteres speciaux autour ou non. On regarde la negation.

                flag=False
                if index_lign>0: #avec un max(0,index_lign-1), si index_lign=0, on va parcourir les elements de la ligne deja etudiee, donc on va trouver au moins 1 digit.
                    for character_up in lign_table[index_lign-1][0][max(0,index_begin-1):min(index_begin+index_end+1,column_number)]:
                        # verification pour les caracteres situes sur la ligne au-dessus de celle etudiee.
                        if not character_up.isdigit() and not character_up=='.':
                            flag=True
                            break
            
                if index_lign<lign_number-1:
                    for character_down in lign_table[index_lign+1][0][max(0,index_begin-1):min(index_begin+index_end+1,column_number)]:
                        # verification pour les caracteres situes sur la ligne en-dessous de celle etudiee.
                        if not character_down.isdigit() and not character_down=='.':
                            flag=True
                            break

                if index_begin>=1:
                    # verification pour le caracteres situe sur la ligne a gauche de la sequence de digits etudiee.
                    if not lign[0][index_begin-1].isdigit() and not lign[0][index_begin-1]=='.':
                        flag=True

                if index_begin+index_end<column_number-1:
                    # verification pour le caracteres situe sur la ligne a droite de la sequence de digits etudiee.
                    if not lign[0][index_begin+index_end].isdigit() and not lign[0][index_begin+index_end]=='.':
                        flag=True

                if flag: # un caractere speciale est present au voisinage proche de la sequence de digits etudiee.
                    intermediate_results.append(lign[0][index_begin:index_begin+index_end])

                index_begin+=index_end # VARIANT DE BOUCLE : index_begin


            else:
                index_begin+=1 # VARIANT DE BOUCLE : index_begin
                        
        index_lign+=1

    print(intermediate_results)
    definitive_results=list(int(x) for x in intermediate_results)

    return (sum(definitive_results),'Fini')


#print(new_analyse_matrice(test_2)) # resultat : 925 : OK !
#print(newanalyse_matrice([ligne11,ligne12,ligne13]))

def new_solve(fichier):
    """Renvoie la somme des nombres contenus dans le fichier en argument qui verfient la propriete suivante :
    il existe un caractere special dans l'entourage proche de ces nombres."""
    liste_input=lecture_fichier(fichier)[0]
    return new_analyse_matrice(liste_input)

print(new_solve('input.txt')) # resultat : 556 367 : OK !