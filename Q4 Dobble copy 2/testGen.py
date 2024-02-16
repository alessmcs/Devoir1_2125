def generate(order):
    n = order

    tab1 = []
    # Ajouter n tableaux vides qui seront de taille n pour avoir un tableau nxn 
    for i in range(n):  # n rangées
        rangee = []
        for j in range(n):  # n colonnes
            rangee.append([])
        tab1.append(rangee)

    tab2 = []  # Tableau de taille (n+1)x1 (l'horizon)
    # Ajouter n+1 tableaux vides 
    for i in range(n+1):
        tab2.append([])

    # Liste de symboles agit comme une pile, n^2+n+1 symboles possibles
    symboles = []
    nbCartesSymboles = (n**2)+n+1
    for i in range(nbCartesSymboles):
        symboles.append(i)

    # Faire les n premiers symboles 
    for i in range(n):
        s = symboles.pop(0)  # Enlever de la liste
        for j in tab1[i]:  # Rangée du tab1
            j.append(s)
        tab2[0].append(s)

    # 2n prochains symboles
    section = symboles[:n]
    print("section")
    print(section)
    for i in range(n):
        for j in section:
            tab1[i][(section.index(j) + i) % n].append(j)
            tab1[i][(section.index(j) + i) % n].append(symboles[section.index(j) + n])
        tab2[1].append(section[i])
        tab2[2].append(symboles[i + n])

    # Pop les 2n prochains éléments
    for i in range(2 * n):
        symboles.pop(0)

    index = 3
    while len(symboles) > 1:
        # Remplir les colonnes du tab1 en bonds de n
        # Et ajouter au tab2
        for i in range(n):
            s = symboles.pop(0)
            for j in range(n):
                tab1[j][i].append(s) #TODO
            tab2[index].append(s)
        index += 1

    # Dernier élément de symboles -> Remplir l'horizon
    dernierSymbole = symboles.pop(0)
    for i in tab2:
        i.append(dernierSymbole)

    # TODO: À compléter

    # Mélange aléatoire des symboles sur les cartes
    # pour ne pas avoir des répétitions de symboles sur les mêmes endroits des cartes
    # shuffle ihihihihiihi
     # Mélange aléatoire des symboles sur les cartes

    for c in tab1:
        for i in range(len(c)):
            random.shuffle(c[i])
    
    for c in tab2:
        random.shuffle(c)

    # TODO: À compléter

    # Écriture des cartes dans le fichier cards_file
    # Writing cards in the cards_file file

    # TODO: À compléter

generate(3)
