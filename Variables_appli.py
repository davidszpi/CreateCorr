# Copyright ou © ou Copr. David Sanchez, (11/05/2022)

# david.sanchez@insa-toulouse.fr

# Ce logiciel est un programme informatique servant à créer des feuilles au
# format Excel utilisées pour la correction des copies.

# Ce logiciel est régi par la licence [CeCILL|CeCILL-B|CeCILL-C] soumise au
# droit français et respectant les principes de diffusion des logiciels libres.
# Vous pouvez utiliser, modifier et/ou redistribuer ce programme sous les
# conditions de la licence [CeCILL|CeCILL-B|CeCILL-C] telle que diffusée par le
# CEA, le CNRS et l'INRIA sur le site "http://www.cecill.info".

# En contrepartie de l'accessibilité au code source et des droits de copie,
# de modification et de redistribution accordés par cette licence, il n'est
# offert aux utilisateurs qu'une garantie limitée.  Pour les mêmes raisons,
# seule une responsabilité restreinte pèse sur l'auteur du programme,  le
# titulaire des droits patrimoniaux et les concédants successifs.

# A cet égard  l'attention de l'utilisateur est attirée sur les risques
# associés au chargement,  à l'utilisation,  à la modification et/ou au
# développement et à la reproduction du logiciel par l'utilisateur étant
# donné sa spécificité de logiciel libre, qui peut le rendre complexe à
# manipuler et qui le réserve donc à des développeurs et des professionnels
# avertis possédant  des  connaissances  informatiques approfondies.  Les
# utilisateurs sont donc invités à charger  et  tester  l'adéquation  du
# logiciel à leurs besoins dans des conditions permettant d'assurer la
# sécurité de leurs systèmes et ou de leurs données et, plus généralement,
# à l'utiliser et l'exploiter dans les mêmes conditions de sécurité.

# Le fait que vous puissiez accéder à cet en-tête signifie que vous avez
# pris connaissance de la licence [CeCILL|CeCILL-B|CeCILL-C], et que vous en
# avez accepté les termes.

from tkinter import StringVar, IntVar, DoubleVar, BooleanVar, TclError
import tkinter.messagebox as msg
from re import split
# from watchpoints import watch

from utils.utils_liste import *
from utils_excel.creation_excel import Option_Feuille_de_Note


class Variables_appli:

    def __init__(self, nb_max_etudiants, stat, points_par_questions, arrondir):
        self.str_liste_exo = StringVar()
        self.questions = [3]
        # watch(self.questions)
        self.nb_exercices = IntVar()
        self.nb_exercices.set(1)
        self.nom_du_sujet = StringVar()
        self.nb_max_etud = IntVar()
        self.nb_max_etud.set(nb_max_etudiants)
        self.nb_points_sujets = DoubleVar()
        self.nb_points_sujets.set(20)
        self.stat = BooleanVar()
        self.stat.set(stat)
        self.couleur = "#b0ffff"
        self.arrondir = BooleanVar()
        self.arrondir.set(arrondir)
        self.point_par_question = IntVar()
        self.point_par_question.set(points_par_questions)
        self.nb_colonnes_init = IntVar()
        self.nb_colonnes_init.set(2)
        self.colonnes_init = [StringVar(), StringVar()]
        self.colonnes_init[0].set("Nom")
        self.colonnes_init[1].set("Prénom")
        self.Nom_exercices = [StringVar()]
        self.Nom_exercices[0].set("Exercice 1")
        self.Liste_exercices = [[StringVar(), StringVar(), StringVar()]]
        self.Liste_exercices[0][0].set("1)")
        self.Liste_exercices[0][1].set("2)")
        self.Liste_exercices[0][2].set("3)")
        self.Liste_description_exercices = [[StringVar(),
                                             StringVar(),
                                             StringVar()]]
        self.Liste_bareme = [[DoubleVar(), DoubleVar(), DoubleVar()]]
        self.Points_restants = DoubleVar()
        self.Points_restants.set(self.nb_points_sujets.get())

    def validation_format_liste(self):
        # la chaine ne doit contenir que 0123456789 ou des espaces
        ensemble = set("0123456789 ")
        texte = self.str_liste_exo.get()
        test = all([char in ensemble for char in texte])
        # Teste si la liste a le bon format
        if test:
            liste = [int(ch) for ch in split(r'\s', texte) if ch != '']
            if not liste:  # liste vide
                msg.showerror("Liste vide",
                              "Vous n'avez pas rentré d'exercices!")
                return False, liste
            else:
                return True, liste
        else:
            msg.showerror("Erreur de format",
                          ("Le champ liste d'exercice ne doit "
                           "contenir que des chiffres ou des espaces!"))
            return False, []

    def ajoute_exercice(self, nb_questions, reinit=False):
        # ajoute un exercice à la feuille Excel
        # si reinit=True, il ne faut pas mettre à jour questions
        nb_ex = len(self.Nom_exercices)
        if not reinit:
            self.questions.append(nb_questions)
        self.Nom_exercices.append(StringVar())
        self.Nom_exercices[-1].set(f"Exercice {nb_ex+1}")
        self.Liste_exercices.append([])
        self.Liste_description_exercices.append([])
        self.Liste_bareme.append([])
        maj_liste(self.Liste_exercices[nb_ex], nb_questions,
                  add_variable, StringVar)
        for i in range(nb_questions):
            self.Liste_exercices[nb_ex][i].set(f"{i+1})")
        maj_liste(self.Liste_description_exercices[nb_ex], nb_questions,
                  add_variable, StringVar)
        maj_liste(self.Liste_bareme[nb_ex], nb_questions,
                  add_variable, DoubleVar)
        self.nb_exercices.set(nb_ex+1)

    def supprime_exercice(self, num):
        nb_ex = len(self.Nom_exercices)
        if num > nb_ex:
            msg.showerror("Erreur", f"Il n'y a pas d'exercice n°{num}")
        else:
            del self.Nom_exercices[num]
            del self.Liste_exercices[num]
            del self.Liste_description_exercices[num]
            del self.Liste_bareme[num]
            del self.questions[num]
            self.nb_exercices.set(len(self.questions))

    def swap_exercice(self, num1, num2):
        nb_ex = len(self.Nom_exercices)
        if num1 > nb_ex or num2 > nb_ex:
            msg.showerror("Erreur",
                          f"Il n'y a pas d'exercice n°{max(num1, num2)}")
        else:
            (self.Nom_exercices[num1], self.Nom_exercices[num2]) = (
                self.Nom_exercices[num2], self.Nom_exercices[num1])
            (self.Liste_exercices[num1], self.Liste_exercices[num2]) = (
                self.Liste_exercices[num2], self.Liste_exercices[num1])
            (self.Liste_description_exercices[num1],
             self.Liste_description_exercices[num2]) = (
                self.Liste_description_exercices[num2],
                self.Liste_description_exercices[num1])
            (self.Liste_bareme[num1], self.Liste_bareme[num2]) = (
                self.Liste_bareme[num2], self.Liste_bareme[num1])

    def modifie_nb_questions(self, exercice, num):
        maj_liste(self.Liste_exercices[exercice], num, add_variable, StringVar)
        maj_liste(self.Liste_description_exercices[exercice], num,
                  add_variable, StringVar)
        maj_liste(self.Liste_bareme[exercice], num, add_variable, DoubleVar)
        n = len(self.Liste_exercices[exercice])
        for i in range(n-num, n):
            self.Liste_exercices[exercice][i].set(f'{i+1})')

    def maj_exercices(self, liste_exo, reinit=False):
        # En fonction de liste exercice, met à jour self
        # si reinit = True, il ne faut pas rajouter les exercices
        # dans questions, il y sont déjà
        nb_exercice = len(liste_exo)
        nb_exercice_actuel = len(self.Nom_exercices)
        maj = True
        # Ajuste le nombre d'exercices
        # Ne prévient que si on en supprime
        if nb_exercice_actuel < nb_exercice:
            for i in range(nb_exercice_actuel, nb_exercice):
                self.ajoute_exercice(liste_exo[i], reinit)
        elif nb_exercice_actuel > nb_exercice:
            maj = msg.askokcancel(
                "Le nombre d'exercices a diminué",
                "Mettre à jour? (cela supprimera les derniers exercices)")
            if maj:
                for i in range(nb_exercice_actuel, nb_exercice, -1):
                    self.supprime_exercice(i-1)
        # Ajuste le nombre de questions des exercices
        # Doit parcourir tous les exercices pour vérifier si le nombre
        # de questions est le bon
        if maj:
            exercices_actuels = [len(liste) for liste in self.Liste_exercices]
            liste_diff = [a-b for a, b in zip(liste_exo,
                                              exercices_actuels)]
            test = all([x == 0 for x in liste_diff])
            if not test:
                if msg.askokcancel(
                    "Le nombre de questions des exercices a changé",
                    ("Mettre à jour? (cela peut entraîner "
                     "des pertes de données)")):
                    for i in range(nb_exercice):
                        self.modifie_nb_questions(i, liste_diff[i])

    def test_format_variables(self, Feuille_excel: Option_Feuille_de_Note):
        # Teste si toutes les listes de self ont la même taille que celles
        # de Feuille_excel
        # True si vrai, False sinon
        test = True
        test = test and (self.nb_colonnes_init.get()
                         == len(Feuille_excel.colonnes_initiales))
        test = test and (len(self.Nom_exercices)
                         == len(Feuille_excel.liste_questions))
        test = test and all([len(self.Liste_exercices[i]) == nb
                             for i, nb in enumerate(
                                 Feuille_excel.liste_questions)])
        return test

    def initialise_variable(self, Feuille_excel: Option_Feuille_de_Note):
        # initialise_colonnes_initiales
        self.colonnes_init = [StringVar()
                              for _ in Feuille_excel.colonnes_initiales]
        for i, texte in enumerate(Feuille_excel.colonnes_initiales):
            self.colonnes_init[i].set(texte)
        # initialise toutes les variables de self avec les données
        # de Feuille_excel si elles ont le même format
        if self.test_format_variables(Feuille_excel):
            self.nom_du_sujet.set(Feuille_excel.nom_du_sujet)
            self.nb_max_etud.set(Feuille_excel.nb_max_etud)
            self.stat.set(Feuille_excel.stat)
            self.arrondir.set(Feuille_excel.arrondir)
            self.point_par_question.set(Feuille_excel.point_par_question)
            for i, val in enumerate(Feuille_excel.colonnes_initiales):
                self.colonnes_init[i].set(val)
            self.nb_colonnes_init.set(len(self.colonnes_init))
            for i, nom in enumerate(Feuille_excel.Nom_exercices):
                self.Nom_exercices[i].set(nom)
            for i, liste in enumerate(Feuille_excel.Liste_exercices):
                for j, val in enumerate(liste):
                    self.Liste_exercices[i][j].set(val)
            for i, liste in enumerate(
                    Feuille_excel.Liste_description_exercices):
                for j, val in enumerate(liste):
                    self.Liste_description_exercices[i][j].set(val)
            for i, liste in enumerate(Feuille_excel.Liste_bareme):
                for j, val in enumerate(liste):
                    self.Liste_bareme[i][j].set(val)

    def points_attribues(self):
        somme = 0.
        for liste in self.Liste_bareme:
            for variable in liste:
                try:
                    x = variable.get()
                except TclError:
                    x = 0
                somme += x
        return somme

    def traceur_bareme(self, a, b, c):
        # Variables requises mais inutilisées dans notre cas
        # Cette fonction est appelée pour mettre à jour le
        # label points restants
        try:
            x = self.nb_points_sujets.get()
        except TclError:
            x = 0
        self.Points_restants.set(
            f'{x-self.points_attribues()}')

    def effacer_trace(self, variable):
        for trace in variable.trace_vinfo():
            variable.trace_vdelete(*trace)
