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

from re import X
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import asksaveasfilename
import tkinter.messagebox as msg
from functools import partial

from utils_excel.creation_excel import Option_Feuille_de_Note
from api.gestion_onglets import Onglets
from utils.run import run_file
from afficher_licence import Afficher_licence

from Variables_appli import Variables_appli


class Appli(tk.Tk):

    def __init__(self, nb_max_etud=28,
                 stat=True, point_par_question=4,
                 arrondir=False):

        tk.Tk.__init__(self)
        self.frame = ttk.Frame(self)
        self.title("Création de feuilles de correction")
        self.iconphoto(False, tk.PhotoImage(file='logo.png'))
        style = ttk.Style(self)
        style.theme_use('alt')

        self.VarApp = Variables_appli(nb_max_etud,
                                      stat,
                                      point_par_question,
                                      arrondir)
        # self.frame_entete = ttk.Frame(self.frame)
        # self.l_titre = ttk.Label(
        #     self.frame_entete, text="Création de feuilles de correction")
        self.Onglets = Onglets(self.VarApp, self.frame)
        # Frame de boutons visibles pour tout onglet
        self.frame_bouton = ttk.Frame(self.frame)
        b_creation = ttk.Button(
            self.frame_bouton,
            text="Création du fichier Excel",
            command=partial(creation, self.VarApp))
        b_quit = ttk.Button(self.frame_bouton, text="Quitter",
                            command=self.quit)
        b_creation.pack(side=tk.LEFT, padx=5, pady=5)
        b_quit.pack(side=tk.RIGHT, padx=5, pady=5)

        # Menu
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Créer le fichier Excel",
                              command=lambda: creation(self.VarApp))
        file_menu.add_command(label="Voir la licence",
                              command=lambda: Afficher_licence(self))
        file_menu.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)

        # Placement
        self.config(menu=menu_bar)

        # Placer les frames
        # self.l_titre.pack(expand=True)
        # self.frame_entete.pack(expand=True)
        self.Onglets.pack()
        self.frame_bouton.pack(expand=True)
        self.frame.pack(expand=True)

        self.mainloop()


def creation(VarApp: Variables_appli):
    Feuille_excel = Option_Feuille_de_Note(
        VarApp.nom_du_sujet.get(),
        [item.get() for item in VarApp.colonnes_init],
        VarApp.questions,
        VarApp.nb_max_etud.get(),
        VarApp.point_par_question.get(),
        [item.get() for item in VarApp.Nom_exercices],
        [[item.get() for item in liste]
            for liste in VarApp.Liste_exercices],
        [[item.get() for item in liste]
            for liste in VarApp.Liste_description_exercices],
        [[item.get() for item in liste] for liste in VarApp.Liste_bareme],
        VarApp.couleur,
        VarApp.arrondir.get(),
        VarApp.stat.get(),
        )
    filename = asksaveasfilename(
        defaultextension='.xlsx', title="Enregistrer sous")
    # print(Options)
    wb = Feuille_excel.Create_Feuille_de_notes()
    wb.save(filename)
    if msg.askyesno(title="Création du fichier réussie",
                    message="Ouvrir le fichier Excel?"):
        run_file(filename)


def main():
    Appli()


if __name__ == '__main__':
    main()
