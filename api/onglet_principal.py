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

import tkinter.ttk as tk

from Variables_appli import Variables_appli
from api.selection_couleur import Selection_couleur
from api.creation_interface import Creation_Interface
from api.fenetre_rapid_conf import RapidConf


class Onglet_Principal(tk.Frame):

    def __init__(self, VarApp: Variables_appli, boss=None):
        tk.Frame.__init__(self, master=boss)
        # text="Configuration du sujet")

        # Création des composants
        # Textes
        self.text_b_color = tk.Label(
            self, text="Couleur utilisée pour colorier 1 ligne sur 2")
        self.text_b_stat = tk.Label(
            self, text="Ajouter moyenne et écart-type")
        # text_b_arrondir = tk.Label(
        #     self, text = "Arrondir au 1/4 de point supérieur")
        self.text_nb_exercices = tk.Label(
            self,
            text="Nombre d'exercices du sujet")
        self.text_entree_nom_sujet = tk.Label(
            self, text='Entrez le nom du sujet')
        self.text_entree_nb_max = tk.Label(
            self, text="Entrez le nombre maximum d'étudiants")
        self.text_entree_nb_points_sujet = tk.Label(
            self, text="Entrez le nombre total de points du sujet")
        self.text_choix_points = tk.Label(
            self, text="Chaque question est notée sur 1 ou 4.")
        # text_vide = tk.Label(self, text= " ")

        # Boutons
        def sauver_couleur(couleur, VarApp: Variables_appli):
            VarApp.couleur = couleur
        self.b_color = Selection_couleur(
            self, VarApp.couleur,
            lambda coul: sauver_couleur(coul, VarApp)
            )
        self.b_rapid_conf = RapidConf(VarApp, self)
        # Boutons à cocher
        self.b_stat = tk.Checkbutton(self, variable=VarApp.stat)

        # Saisies
        self.entree_nb_exercices = tk.Spinbox(
            self, textvariable=VarApp.nb_exercices,
            format='%1.0f', from_=1, to=100, increment=1,
            state='readonly',
            command=lambda: self.update_exercice(VarApp))
        self.entree_nom_du_sujet = tk.Entry(
            self, textvariable=VarApp.nom_du_sujet)
        self.entree_nb_max_etudiants = tk.Spinbox(
            self, textvariable=VarApp.nb_max_etud,
            format='%3.0f', from_=1, to=999, increment=1)
        self.entree_nb_points_sujet = tk.Entry(
            self, textvariable=VarApp.nb_points_sujets)
        self.choix_point_par_question = tk.Spinbox(
            self, textvariable=VarApp.point_par_question,
            format='%1.0f', from_=1, to=4, increment=3)
        VarApp.nb_points_sujets.trace(
            'w', lambda a, b, c: VarApp.traceur_bareme(a, b, c))
        # Création de l'interface
        self.creation()

    def creation(self):
        # Liste de widget. Chaque élément est une liste de widget
        # correspondant à une ligne
        liste_widget = [[self.text_entree_nom_sujet,
                         self.entree_nom_du_sujet],
                        [self.text_entree_nb_max,
                         self.entree_nb_max_etudiants],
                        [self.text_entree_nb_points_sujet,
                         self.entree_nb_points_sujet],
                        [self.text_choix_points,
                         self.choix_point_par_question],
                        [self.text_b_stat, self.b_stat],
                        [self.b_rapid_conf],
                        [self.text_nb_exercices, self.entree_nb_exercices],
                        [self.text_b_color, self.b_color]]
        # Liste des paramètres autres que row et column :
        # columnspan, pady, sticky
        param_widget = [[(1, 3, 'w'), (1, 3, 'ew')],    # nom du sujet
                        [(1, 3, 'w'), (1, 3, 'ew')],    # nb max étudiants
                        [(1, 3, 'w'), (1, 3, 'ew')],    # nb points du sujet
                        [(1, 3, 'w'), (1, 3, 'ew')],    # Points par question
                        [(1, 3, 'w'), (1, 3, 'w')],     # Statistiques
                        [(2, 3, '')],                   # Rapid conf
                        [(1, 3, 'w'), (1, 3, 'w')],     # Nb exercices
                        [(1, 3, 'w'), (1, 3, 'ew')]]    # Choix couleur
        Creation_Interface(liste_widget, param_widget)

    def update_exercice(self, VarApp: Variables_appli):
        old_nb_ex = len(VarApp.Nom_exercices)
        new_nb_ex = VarApp.nb_exercices.get()
        if new_nb_ex > old_nb_ex:
            for j in range(old_nb_ex, new_nb_ex):
                self.master.ajoute_exercice(1, VarApp)
        elif new_nb_ex < old_nb_ex:
            for j in range(old_nb_ex-1, new_nb_ex-1, -1):
                self.master.efface_exercice(j, VarApp)
