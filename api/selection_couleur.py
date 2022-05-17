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

from tkinter.colorchooser import askcolor
from sys import platform
if platform.startswith('dar'):
    import tkmacosx as tk
else:
    import tkinter as tk


class Selection_couleur(tk.Button):
    # Crée un bouton dans frame permettant de choisir la couleur
    # et mettant automatiquement à jour la couleur du bouton
    # avec la couleur sélectionnée

    def __init__(self, fenetre, couleur, action):
        tk.Button.__init__(self, master=fenetre, bg=couleur)
        self.couleur = couleur
        self.action = action
        self.configure(command=self.choix_couleur)

    def choix_couleur(self):
        couleur_select = askcolor(initialcolor=self.couleur)
        # on ne garde que le code hexadécimal de la couleur
        self.couleur = couleur_select[1]
        # Change la couleur du bouton
        self.configure(bg=self.couleur)
        self.action(self.couleur)
        # exécute une action extérieure liée à la couleur
