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
import tkinter.ttk as ttk

from Variables_appli import Variables_appli


class Onglet_exercice(ttk.Frame):

    def __init__(self, VarApp: Variables_appli, numero_exercice,
                 boss=None):
        ttk.Frame.__init__(self, master=boss)
        self.maitre = boss
        self.numero_exercice = numero_exercice
        self.nb_questions = tk.IntVar()
        self.liste_w_text = []
        self.liste_w_intitut = []
        self.liste_w_descr = []
        self.liste_w_bareme = []

        self.nb_questions.set(VarApp.questions[self.numero_exercice])
        # Création des items
        ttk.Label(self, text="Nom de l'exercice : "
                  ).grid(row=0, column=0, sticky='w', pady=6)
        ttk.Entry(self, textvariable=VarApp.Nom_exercices[self.numero_exercice]
                  ).grid(row=0, column=1, sticky='ew', pady=6, columnspan=3)
        ttk.Label(self, text="Nombre de questions : "
                  ).grid(row=1, column=0, sticky='w', pady=6)
        ttk.Spinbox(
            self, textvariable=self.nb_questions,
            format='%1.0f', from_=1, to=10, increment=1,
            state='readonly',
            command=lambda: self.maj_exercice(VarApp)
            ).grid(row=1, column=1, sticky='w', pady=6)
        # Ajoute un bouton pour supprimer l'exercice
        ttk.Button(self, text="Supprimer l'exercice",
                   command=lambda: self.supprimer_exercice(VarApp)
                   ).grid(row=1, column=3)
        ttk.Label(self, text="Nombre total de points restants à distribuer : "
                  ).grid(row=2, column=0, sticky='w', pady=3, columnspan=3)
        ttk.Label(self, textvariable=VarApp.Points_restants,
                  ).grid(row=2, column=3, sticky='w', pady=3)
        # Frame dynamique
        self.frame = ttk.Frame(self)
        # Configuration de la taille des colonnes ne fonctionne pas
        # self.frame.columnconfigure(0, weight=1)
        # self.frame.columnconfigure(1, weight=1)
        # self.frame.columnconfigure(2, weight=5)
        # self.frame.columnconfigure(3, weight=1)
        ttk.Label(self.frame, text="Nom").grid(row=0, column=1,
                                               sticky='nsew')
        ttk.Label(self.frame, text="Description").grid(row=0, column=2,
                                                       sticky='nsew')
        ttk.Label(self.frame, text="Barème").grid(row=0, column=3,
                                                  sticky='nsew')
        for j, _ in enumerate(
                VarApp.Liste_exercices[self.numero_exercice]):
            # Création des widgets (dans une liste)
            self.creation_ligne_w(j, VarApp)
        self.frame.grid(row=3, columnspan=4, column=0)
        # Applique la fonction trace à chaque modification
        # des cases titre exercice
        VarApp.Nom_exercices[self.numero_exercice].trace(
            'w', lambda a, b, c: self.traceur_titre_onglets(a, b, c, VarApp))
        for variable in VarApp.Liste_bareme[self.numero_exercice]:
            variable.trace(
                'w', lambda a, b, c: VarApp.traceur_bareme(a, b, c))

    # Modification des titres des onglets.
    def traceur_titre_onglets(self, a, b, c, VarApp: Variables_appli):
        # Variables requises mais inutilisées dans notre cas
        self.maitre.tab(self.numero_onglet(), text=VarApp.Nom_exercices[
            self.numero_exercice].get())

    def creation_ligne_w(self, j, VarApp: Variables_appli):
        self.liste_w_text.append(ttk.Label(self.frame,
                                           text=f"Question {j+1}"))
        self.liste_w_intitut.append(
            ttk.Entry(self.frame, textvariable=VarApp.Liste_exercices[
                self.numero_exercice][j]))
        self.liste_w_descr.append(
            ttk.Entry(self.frame,
                      textvariable=VarApp.Liste_description_exercices[
                          self.numero_exercice][j]))
        self.liste_w_bareme.append(
            ttk.Entry(self.frame, textvariable=VarApp.Liste_bareme[
                self.numero_exercice][j]))
        # Placement des widgets
        self.liste_w_text[-1].grid(row=j+1, column=0, sticky='nsew',
                                   ipadx=3, padx=3)
        self.liste_w_intitut[-1].grid(row=j+1, column=1,
                                      sticky='nsew', pady=3,
                                      ipadx=3, padx=3)
        self.liste_w_descr[-1].grid(row=j+1, column=2, sticky='nsew', pady=3,
                                    ipadx=3, padx=3)
        self.liste_w_bareme[-1].grid(row=j+1, column=3,
                                     sticky='nsew', pady=3, ipadx=3, padx=3)

    def delete_ligne(self, j, VarApp: Variables_appli):
        VarApp.effacer_trace(VarApp.Liste_bareme[self.numero_exercice][j])
        self.liste_w_text[j].destroy()
        self.liste_w_intitut[j].destroy()
        self.liste_w_descr[j].destroy()
        self.liste_w_bareme[j].destroy()
        del self.liste_w_text[j]
        del self.liste_w_intitut[j]
        del self.liste_w_descr[j]
        del self.liste_w_bareme[j]
        del VarApp.Liste_exercices[self.numero_exercice][j]
        del VarApp.Liste_description_exercices[self.numero_exercice][j]
        del VarApp.Liste_bareme[self.numero_exercice][j]
        VarApp.traceur_bareme(None, None, None)

    def maj_exercice(self, VarApp: Variables_appli):
        new_nb = self.nb_questions.get()
        old_nb = VarApp.questions[self.numero_exercice]
        if new_nb > old_nb:
            for j in range(old_nb, new_nb):
                # ajoute les variables puis crée la ligne
                VarApp.Liste_exercices[
                    self.numero_exercice].append(tk.StringVar())
                VarApp.Liste_description_exercices[
                    self.numero_exercice].append(tk.StringVar())
                VarApp.Liste_bareme[
                    self.numero_exercice].append(tk.DoubleVar())
                self.creation_ligne_w(j, VarApp)
                VarApp.Liste_bareme[
                    self.numero_exercice][-1].trace(
                        'w', lambda a, b, c: VarApp.traceur_bareme(a, b, c))
        elif new_nb < old_nb:
            for j in range(old_nb-1, new_nb-1, -1):
                self.delete_ligne(j, VarApp)
        VarApp.questions[self.numero_exercice] = new_nb

    def supprimer_exercice(self, VarApp: Variables_appli):
        # Calcul du nouveau numéro de l'exercice si
        # des suppressions ont eu lieu avant
        self.numero_exercice = self.numero_onglet()\
            - self.master.nb_onglets_fixes
        self.master.efface_exercice(self.numero_exercice, VarApp)
        # Mettre à jour toutes les traces sur les sujets des exercices
        # On supprime les traces
        for vartitre in VarApp.Nom_exercices:
            VarApp.effacer_trace(vartitre)
        # On les recrée
        for vartitre in VarApp.Nom_exercices:
            vartitre.trace(
                'w',
                lambda a, b, c: self.traceur_titre_onglets(a, b, c, VarApp))
        # Mise à jour de tous les numéros d'exercices ?
        # A rajouter éventuellement

    def numero_onglet(self):
        return self.master.index('current')
