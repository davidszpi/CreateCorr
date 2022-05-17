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


class Widget_colonne_ini(ttk.Frame):

    def __init__(self, VarApp: Variables_appli, boss=None):
        ttk.Frame.__init__(self, master=boss)
        # , text="Colonnes initiales du fichier Excel")
        self.text_colonnes_initiales = ttk.Label(self, text="Nombre : ")
        self.choix_nb_colonne_ini = ttk.Spinbox(
            self, textvariable=VarApp.nb_colonnes_init,
            format='%1.0f', from_=1, to=10, increment=1,
            state='readonly',
            command=lambda: self.update_colonne_ini(VarApp))

        self.nb_colonnes = VarApp.nb_colonnes_init.get()
        self.Liste_entree_colonne_ini = []
        self.Liste_colonnes_initiales = []
        for i in range(self.nb_colonnes):
            self.Liste_entree_colonne_ini.append(
                ttk.Label(self, text=f"Colonne {i+1} : "))
            self.Liste_colonnes_initiales.append(
                ttk.Entry(self, textvariable=VarApp.colonnes_init[i]))
        self.creation()

    def creation(self):
        row = 0
        # Ajout des éléments fixes
        self.text_colonnes_initiales.grid(row=row, column=0,
                                          sticky='ew', pady=3)
        self.choix_nb_colonne_ini.grid(row=row, column=1, sticky='ew', pady=3)
        row = 1
        # Ajout des éléments dynamiques
        for col, liste_colonne in enumerate(
                [self.Liste_entree_colonne_ini,
                 self.Liste_colonnes_initiales]):
            for ligne, elem in enumerate(liste_colonne):
                elem.grid(row=row+ligne, column=col, sticky='ew', pady=3)

    def update_colonne_ini(self, VarApp: Variables_appli):
        nb = VarApp.nb_colonnes_init.get()
        if nb > self.nb_colonnes:
            for i in range(self.nb_colonnes, nb):
                VarApp.colonnes_init.append(tk.StringVar())
                self.Liste_entree_colonne_ini.append(
                    ttk.Label(self, text=f"Colonne {i+1} : "))
                self.Liste_colonnes_initiales.append(
                    ttk.Entry(self, textvariable=VarApp.colonnes_init[i]))
                self.Liste_entree_colonne_ini[i].grid(row=1+i, column=0,
                                                      sticky='ew', pady=3)
                self.Liste_colonnes_initiales[i].grid(row=1+i, column=1,
                                                      sticky='ew', pady=3)
        elif nb < self.nb_colonnes:
            for i in range(self.nb_colonnes-1, nb-1, -1):
                self.Liste_entree_colonne_ini[i].destroy()
                self.Liste_colonnes_initiales[i].destroy()
                del VarApp.colonnes_init[i]
                del self.Liste_entree_colonne_ini[i]
                del self.Liste_colonnes_initiales[i]
        self.nb_colonnes = nb
