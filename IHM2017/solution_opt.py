# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:26:28 2016

@author: osswald
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets,uic
from interface import Ui_principale_ihm
from insectes5 import Ecosysteme

# l'approche par héritage simple de classe QMainWindow (même type de notre fenêtre
# créée avec QT Designer. Nous configurons après l'interface utilisateur
# dans le constructeur (la méthode init()) de notre classe
class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ecopainter = QtGui.QPainter() 
        
        # Configuration de l'interface utilisateur.
        self.ui = uic.loadUi("interface.ui", self)
        # self.ui = Ui_principale_ihm()
        # self.ui.setupUi(self)
        self.ui.bouton_gen.clicked.connect(self.generer)
        self.ui.bouton_sim.clicked.connect(self.simu)
        self.ui.bouton_pas.clicked.connect(self.un_tour)
        
        self.ui.conteneur.paintEvent = self.drawecosysteme
         
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.un_tour)

        pixmap = QtGui.QPixmap("arrierPlan.png")
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.ui.conteneur.lower()
        self.ui.conteneur.stackUnder(self)
        self.ui.conteneur.setAutoFillBackground(True)
        self.ui.conteneur.setPalette(pal)
        
        # palette = QtGui.QPalette()
        # pixmap = QtGui.QPixmap("arrierPlan.png")
        # palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        # self.ui.conteneur.setPalette(palette)
        # Configuration du modèle
        self.generer()
        
        
    def pr_gen(self):
        print("Généré")

    def pr_sim(self):
        print("Simulé")

    def pr_unt(self):
        print("Tourné")

    def generer(self):
        self.ecosys = Ecosysteme(50, 500, self.ui.conteneur.width(), self.ui.conteneur.height())
        self.ui.conteneur.update()

    def simu(self):
        print("Simulation en cours")
        self.timer.start(100)

    def un_tour(self):
        if self.ecosys.nbtour > 0:
            print("Tourné")
            self.ecosys.unTour()
            self.ecosys.nbtour -= 1
            self.ui.conteneur.update() # nécessaire pour la MAJ de l’IHM
        else:
            self.timer.stop()
            print("Fini")
            
    def drawecosysteme(self, *args):
        self.ecopainter.begin(self.ui.conteneur)
        self.ecopainter.setPen(QtCore.Qt.red)
        for ins in self.ecosys:
            ins.dessinimage(self.ecopainter)
        self.ecopainter.end()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    sys.exit(app.exec_())