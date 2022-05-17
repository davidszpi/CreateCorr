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


def Afficher_licence(master=None):
    window = tk.Toplevel(master)
    window.title("Licence")
    frame = ttk.Frame(window)
    text_widget = tk.Text(frame)
    with open("INFO.txt", mode='r', encoding='utf-8') as f:
        text_widget.insert("insert", f.read())
    text_widget.config(height=11)
    text_widget.pack()

    frame2 = ttk.Frame(frame)
    text_widget2 = tk.Text(frame2)
    text_widget2.pack(side="left")
    with open("LICENCE.txt", mode='r', encoding='utf-8') as f:
        text_widget2.insert("insert", f.read())

    scroll_y = tk.Scrollbar(frame2, orient="vertical",
                            command=text_widget.yview)
    scroll_y.pack(side="left", expand=True, fill="y")

    text_widget2.configure(yscrollcommand=scroll_y.set)
    frame2.pack()

    ttk.Button(frame, text="Quitter", command=window.destroy).pack()

    frame.pack()
