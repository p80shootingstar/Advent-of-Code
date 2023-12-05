# Advent of Code

# Problem 1

def lecture_fichier(fichier):
    """Lis le fichier donné en entrée et renvoie son contenu sous la forme d'un
    tableau de chaines de caracteres. 
    Chaque chaine de caractere est une ligne du fichier passe en argument.
    Renvoie en second le nombre de lignes du fichier."""

    chemin='C:/Users/nicol/OneDrive/Documents/Informatique/advent_of_code/pb_1/'
    F=open(chemin+fichier,'r')

    liste_chaine_caracteres=list()
    for ligne in F:
        liste_chaine_caracteres.append(ligne.split())
    return list([liste_chaine_caracteres, len(liste_chaine_caracteres)])

#print(lecture_fichier("input.txt"))

def nettoyage(fichier):
    """Renvoie un tableau contenant les nombres formes par la lecure de gauche a droite 
    des chiffres contenus dans le fichier passe en argument.
    Ce tableau contient des chaines de caracteres.
    Sa longueu, renvoyee en second, est le nombre de lignes du fichier passe en argument."""

    tableau,n=lecture_fichier(fichier)[0],lecture_fichier(fichier)[1]# tableau initial, produit par la lecture du fichier passe en argument.
    tableau_resultat=list(['']*n) # un tableau vide de longueur egale a celle du tableau initial.

    # Construction du tableau renvoye en resultat en 2 etapes : 
    # 1- repere les chiffres parmi les caracteres de chaque ligne.
    # 2- creer une chaine de caracteres qui ne contient que les chiffres reperes a l'etape 1. Etape de nettoyage.
    for k in range(n):
        for ligne in tableau[k]: #chaque ligne est passee en revue...
            for caractere in ligne: #... caractere par acaractere.
                if caractere in ['1','2','3','4','5','6','7','8','9','0']:
                # etape 1 : le caractere trouve est un chiffre : on le garde.
                    tableau_resultat[k]=str(tableau_resultat[k]+caractere) 
                    # etape 2 : Nettoyage.
    return list([tableau_resultat,n])

#print(nettoyage('input.txt'))

def tableau_calibration_doc(fichier):
    """Renvoie un tableau contenant les nombres de calibrations.
    Ces nombres sont formes de deux digits, a partir du tableau nettoye des caractères non numeriques.
    Le tableau renvoye contient des chaines de caracteres."""
    tableau_nettoye,n=nettoyage(fichier)[0], nettoyage(fichier)[1] # recuperation du tableau nettoye : i.e. avec uniquement les chiffres de chaque ligne, lus de gauche a droite.
    tableau_resultat=tableau_nettoye # creation du tableau resultat, copie du tableau nettoye (donc de longueur egale au nombre de lignes du fichier).

    for k in range(n):
        if len(tableau_nettoye[k])==1:
            # Cas 1 : 1 seul chiffre sur la ligne. Chiffre a repeter 2 fois pour obtenir le nombre de calibration.
            tableau_resultat[k]=tableau_nettoye[k][0]*2
        elif len(tableau_nettoye[k])>=3:
            # Cas 2 : strictement plus de 2 chiffres sur la ligne. On garde le premier et le dernier pour former le nombre de calibration.
            tableau_resultat[k]=tableau_nettoye[k][0]+tableau_nettoye[k][-1]
    return tableau_resultat, len(tableau_resultat)

#print(tableau_calibration_doc('input.txt'))

def solve(fichier):
    tableau_chaines_caracteres,n=tableau_calibration_doc(fichier)[0],tableau_calibration_doc(fichier)[1]
    tableau_resultat=list([0]*n)

    for k in range(n):
        tableau_resultat[k]=int(tableau_chaines_caracteres[k])
    return sum(tableau_resultat)

print(solve('input.txt'))

# Resultat : 55488 : OK.
