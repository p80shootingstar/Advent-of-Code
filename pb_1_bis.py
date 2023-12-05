# Advent of Code

# Problem 1 - bis

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

mot1='two1nine'
mot2='eightwothree'
mot3='abcone2threexyz'
mot4='xtwone3four'
mot5='4nineeightseven2'
mot6='zoneight234'
mot7='7pqrstsixteen'

def recuperateur_chiffres(mot):
    """Renvoie le nombre forme par le mot passe en argument.
    Ce nombre peut etre forme par des chiffres ecrit en numerique (1,2,...), 
    ou en lettres (one, two...).
    Respecte l'ordre dans lequel ces chiffres sont ecrits.
    Renvoie le resultat sous la forme d'un entier."""

    intermediaire=str('')

    n=len(mot)
    for k in range(n): # Tests pour retrouver des chiffres ecrits en lettres.
        # Test pour retrouver 'one'.
        if mot[k]=='o':
            if k+1<n-1 and mot[k+1]=='n':
                if k+2<=n-1 and mot[k+2]=='e':
                    intermediaire=intermediaire+'1'
        # Test pour retrouver 'two'.
        if mot[k]=='t':
            if k+1<n-1 and mot[k+1]=='w':
                if k+2<=n-1 and mot[k+2]=='o':
                    intermediaire=intermediaire+'2'
        # Test pour retrouver 'three'.
        if mot[k]=='t':
            if k+1<n-1 and mot[k+1]=='h':
                if k+2<n-1 and mot[k+2]=='r':
                    if k+3<n-1 and mot[k+3]=='e':
                        if k+4<=n-1 and mot[k+4]=='e':
                            intermediaire=intermediaire+'3'
        # Test pour retrouver 'four'.
        if mot[k]=='f':
            if k+1<n-1 and mot[k+1]=='o':
                if k+2<n-1 and mot[k+2]=='u':
                    if k+3<=n-1 and mot[k+3]=='r':
                        intermediaire=intermediaire+'4'
        # Test pour retrouver 'five'.
        if mot[k]=='f':
            if k+1<n-1 and mot[k+1]=='i':
                if k+2<n-1 and mot[k+2]=='v':
                    if k+3<=n-1 and mot[k+3]=='e':
                        intermediaire=intermediaire+'5'
        # Test pour retrouver 'six'.
        if mot[k]=='s':
            if k+1<n-1 and mot[k+1]=='i':
                if k+2<=n-1 and mot[k+2]=='x':
                    intermediaire=intermediaire+'6'
        # test pour retrouver 'seven'.
        if mot[k]=='s':
            if k+1<n-1 and mot[k+1]=='e':
                if k+2<n-1 and mot[k+2]=='v':
                    if k+3<n-1 and mot[k+3]=='e':
                        if k+4<=n-1 and mot[k+4]=='n':
                            intermediaire=intermediaire+'7'
        # Test pour retrouver 'eight'.
        if mot[k]=='e':
            if k+1<n-1 and mot[k+1]=='i':
                if k+2<n-1 and mot[k+2]=='g':
                    if k+3<n-1 and mot[k+3]=='h':
                        if k+4<=n-1 and mot[k+4]=='t':
                            intermediaire=intermediaire+'8'
        # Test pour retrouver 'nine'.
        if mot[k]=='n':
            if k+1<n-1 and mot[k+1]=='i':
                if k+2<n-1 and mot[k+2]=='n':
                    if k+3<=n-1 and mot[k+3]=='e':
                        intermediaire=intermediaire+'9'

        # Test pour retrouver des chiffres ecrits en numerique.
        if mot[k] in ['1','2','3','4','5','6','7','8','9']:
            intermediaire=intermediaire+mot[k]

    return intermediaire
    
# print(recuperateur_chiffres(mot1))
# print(recuperateur_chiffres(mot2))
# print(recuperateur_chiffres(mot3))
# print(recuperateur_chiffres(mot4))
# print(recuperateur_chiffres(mot5))
# print(recuperateur_chiffres(mot6))
# print(recuperateur_chiffres(mot7))


def nettoyage(fichier):
    """Renvoie un tableau d'entiers contenant les nombres formes par le fichier passe en argument.
    Ces nombre sont formes de chiffres ecrits en numerique (1,2,...) ou en lettres (one, txo,...).
    Ils sont ici traduits en chaine de caracteres."""

    tableau_a_nettoyer,n=lecture_fichier(fichier)[0],lecture_fichier(fichier)[1]
    tableau_resultat=list([0]*n)

    for k in range(n):
        tableau_resultat[k]=recuperateur_chiffres(tableau_a_nettoyer[k][0])

    return (tableau_resultat,n)

# print(nettoyage('input.txt'))

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

# print(tableau_calibration_doc('input.txt'))

def solve(fichier):
    """Renvoie la somme du tableau formes par les nombres de calibration recuperes
    dans le fichier passe en argument.
    Renvoie un entier."""

    tableau_chaines_caracteres,n=tableau_calibration_doc(fichier)[0],tableau_calibration_doc(fichier)[1]
    tableau_resultat=list([0]*n)

    for k in range(n):
        tableau_resultat[k]=int(tableau_chaines_caracteres[k])
    return sum(tableau_resultat)

print(solve('input.txt'))

# Resultat : 55614, OK.
