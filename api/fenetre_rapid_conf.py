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

import tkinter as tk
from tkinter.messagebox import askokcancel, WARNING
import tkinter.ttk as ttk

from Variables_appli import Variables_appli
from api.creation_interface import Creation_Interface


class RapidConf(ttk.Button):

    def __init__(self, VarApp: Variables_appli, boss=None):
        ttk.Button.__init__(self, master=boss,
                            text="Configuration rapide des exercices",
                            command=lambda: self.confirm(VarApp))

    def confirm(self, VarApp: Variables_appli):
        reponse = askokcancel(
            title="Attention",
            message="Cela va effacer la configuration existante des exercices",
            icon=WARNING)
        if reponse:
            self.rapid_conf(VarApp)

    def rapid_conf(self, VarApp: Variables_appli):
        window = tk.Toplevel(self.master)
        window.title("Configuration rapide des exercices")
        frame = ttk.Frame(window)

        def detruire():
            window.destroy()

        def valider():
            self.valider_entree(VarApp)
            detruire()

        text_entre_liste = ttk.Label(
            frame,
            text=(
                "Entrez une suite de nombres séparés par des espaces\n"
                "Chaque valeur correspond au nombre "
                "de questions d'un exercice\n"
                "Exemple: 3 2 4 pour trois exercices de 3, 2 et 4 questions"))
        entree_liste = ttk.Entry(
            frame, textvariable=VarApp.str_liste_exo)
        b_valider = ttk.Button(frame, text="Valider",
                               command=valider)
        b_annuler = ttk.Button(frame, text="Annuler",
                               command=detruire)
        l_widget = [[text_entre_liste],
                    [entree_liste],
                    [b_annuler, b_valider]]
        p_widget = [[(2, 3, 'e')],
                    [(2, 3, 'ew')],
                    [(1, 3, ''), (1, 3, '')]]
        Creation_Interface(l_widget, p_widget)
        entree_liste.focus_set()
        frame.pack()

    def valider_entree(self, VarApp: Variables_appli):
        test, liste = VarApp.validation_format_liste()
        if test:
            # efface tous les exercices précédents
            for i in reversed(range(VarApp.nb_exercices.get())):
                self.master.master.efface_exercice(i, VarApp)
            VarApp.questions = liste
            VarApp.nb_exercices.set(len(liste))
            self.master.master.initialise_exercices(VarApp, True)
