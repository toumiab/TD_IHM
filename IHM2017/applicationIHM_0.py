# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2018

@author: toumiab
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre 
# créée avec QT Designer. Nous configurons après l'interface utilisateur 
# dans le constructeur (la méthode init()) de notre classe

class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('interface.ui', self)
        
        # TO DO
        # Chargement de votre fenetre ui.
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("arrierPlan.png")  # assurer vous que l'image est bien déposée dans le répertoire de projet
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.ui.setPalette(palette)
        
        
        
        
        
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
