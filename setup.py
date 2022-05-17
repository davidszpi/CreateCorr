# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build > output_build.txt

from cx_Freeze import setup, Executable
import subprocess
import sys


# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

NAME = 'CreateCorr'
VERSION = '1.0'
AUTHOR = "David Sanchez"
DESCRIPTION = 'Création de feuilles de correction Excel'
PACKAGES = ['re', 'tkinter', 'tkinter.ttk',
            'tkinter.filedialog', 'tkinter.messagebox', 'functools',
            'dataclasses', 'openpyxl', 'openpyxl.utils',
            'openpyxl.styles', 'subprocess', 'sys', 'os', 'sys',
            'tkinter.colorchooser', 'tkmacosx'
            ]
liste_package_local = ["api", "utils", "utils_excel"]

# 'afficher_licence', 'variable_appli' ]


liste_fichiers = ["logo.png", "logo.ico", "afficher_licence.py",
                  "LICENCE.txt", "LICENSE.txt", "INFO.txt"]

# if names are same just have a string not a tuple
installed_packages = subprocess.check_output(
    [sys.executable, '-m', 'pip', 'freeze']).decode('utf-8')
installed_packages = installed_packages.split('\r\n')
EXCLUDES = {pkg.split('==')[0] for pkg in installed_packages if pkg != ''}
# EXCLUDES.add('tkinter')
for pkg in PACKAGES:
    if type(pkg) == str:
        if pkg in EXCLUDES:
            EXCLUDES.remove(pkg)
    else:
        if pkg[1] in EXCLUDES:
            EXCLUDES.remove(pkg[1])

executables = [Executable(script="createcorr.py",
                          icon="logo.ico",
                          target_name=NAME,
                          base=base)]

liste_pkg = liste_package_local +\
    [pkg if type(pkg) == str else pkg[0] for pkg in PACKAGES]

buildOptions = {'packages': liste_pkg,
                'include_files': liste_fichiers,
                'excludes': EXCLUDES,
                'optimize': 2}


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    options=dict(build_exe=buildOptions),
    executables=executables)
