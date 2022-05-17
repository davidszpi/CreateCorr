from tkinter import Label


def reduit_liste(liste, val):
    # val doit être un entier négatif
    # enleve les |val| dernières clés du liste
    del liste[val:]


def ajoute_liste(liste, liste2):
    liste.extend(liste2)


def maj_liste(liste, valeur, objet, *args):
    # Effectue la maj d'une liste
    # objet est une fonction
    # regarder comment fonctionne les itérateurs pour améliorer?
    if valeur < 0:
        reduit_liste(liste, valeur)
    elif valeur > 0:
        ajoute_liste(liste, [objet(j, *args) for j in range(valeur)])


def add_liste(i):
    return []


def add_label(i, texte, frame, Op_gr):
    # texte: fonction qui crée le texte en fonction du paramètre i
    return Label(frame, text=texte(i), font=(Op_gr.police, 10),
                 bg=Op_gr.bgcouleur, fg=Op_gr.txtcouleur)


def add_variable(i, fonc):
    # fonc peut être IntVar, StringVar, BooleanVar, DoubleVar
    return fonc()
