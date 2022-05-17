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

from tkinter.ttk import Notebook

from Variables_appli import Variables_appli
from api.onglet_principal import Onglet_Principal
from api.onglet_colonne_ini import Widget_colonne_ini
from api.onglet_exercice import Onglet_exercice


class Onglets(Notebook):
    def __init__(self, VarApp: Variables_appli, boss=None):
        Notebook.__init__(self, master=boss)
        self.nb_onglets_fixes = 2
        self.Liste_onglets = []
        # Ajout de l'onglet principal
        onglet_principal = Onglet_Principal(VarApp, self)
        self.Liste_onglets.append(onglet_principal)
        self.add(self.Liste_onglets[-1], text='Configuration du sujet')
        # Ajout de l'onglet configuration des colonnes initiales
        onglet_colonne_init = Widget_colonne_ini(VarApp, self)
        self.Liste_onglets.append(onglet_colonne_init)
        self.add(self.Liste_onglets[-1], text='Colonnes initiales')
        # Ajout des onglets pour chaque exercice
        self.initialise_exercices(VarApp)

    def initialise_exercices(self, VarApp: Variables_appli, reinit=False):
        VarApp.maj_exercices(VarApp.questions, reinit)
        print(VarApp.questions)
        for i in range(VarApp.nb_exercices.get()):
            self.Liste_onglets.append(
                Onglet_exercice(VarApp, i, self))
            self.add(self.Liste_onglets[-1],
                     text=VarApp.Nom_exercices[i].get())

    def ajoute_exercice(self, nb_questions, VarApp: Variables_appli):
        # ajoute un exercice en dernière position
        num_exo = len(VarApp.Liste_exercices)
        VarApp.ajoute_exercice(nb_questions)
        self.Liste_onglets.append(
            Onglet_exercice(VarApp, num_exo, self))
        self.add(self.Liste_onglets[-1],
                 text=VarApp.Nom_exercices[num_exo].get())

    def efface_exercice(self, i, VarApp: Variables_appli):
        for variable in VarApp.Liste_bareme[i]:
            VarApp.effacer_trace(variable)
        VarApp.effacer_trace(VarApp.Nom_exercices[i])
        VarApp.supprime_exercice(i)
        self.forget(i+self.nb_onglets_fixes)
        self.Liste_onglets[i+self.nb_onglets_fixes].destroy()
        del self.Liste_onglets[i+self.nb_onglets_fixes]
        VarApp.traceur_bareme(None, None, None)
