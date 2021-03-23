# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2017

@author: toumiab
"""

import sys
from PyQt5 import QtWidgets, QtGui, QtCore 
from interface import Ui_principale_ihm
from ecosysteme import Ecosysteme

# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre 
# créée avec QT Designer. Nous configurons après l'interface utilisateur 
# dans le constructeur (la méthode init()) de notre classe

class MonAppli(QtWidgets.QMainWindow):  # Q 3
    def __init__(self):
        super().__init__()
        # Configuration de l'interface utilisateur.
        # Q4
        self.ui = Ui_principale_ihm()
        self.ui.setupUi(self)
        # ----------
        # Q9 : ajout de l'arriere Plan
        pal = QtGui.QPalette()
        pixmap = QtGui.QPixmap("arrierPlan.png")
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        self.ui.conteneur.lower()
        self.ui.conteneur.stackUnder(self)
        self.ui.conteneur.setAutoFillBackground(True)
        self.ui.conteneur.setPalette(pal)
        self.painter= QtGui.QPainter(self)
        # ----------------------------------------
        
        #----------------Q5
        y = self.ui.conteneur.height()
        x=  self.ui.conteneur.width()
        self.ecosys = Ecosysteme(300,150,60, x,y)
        # Q6 : Connexion entre lles boutons et les méthodes
        # 
        self.ui.bouton_pas.clicked.connect(self.un_pas) 
        self.ui.bouton_gen.clicked.connect(self.generer) 
        self.ui.bouton_sim.clicked.connect(self.simuler)
        
    def un_pas(self) :
        print("un pas")
        # Q8 -----------------------------------------------
        self.ecosys.unTour()
        self.ui.centralwidget.update()

    def generer(self) :
        print("Genérer")
        # Q7 -----------------------------------------------
        self.ecosys=Ecosysteme(60,50,100, self.ui.conteneur.width(),self.ui.conteneur.height())
        self.ui.centralwidget.update()
    
    def simuler(self):
        print("Simuler")
        # Q8 -----------------------------------------------
        self.ecosys.simuler()
        self.ui.centralwidget.update()
        
    # Question Partie II.1 ----------------------
    def paintEvent(self, e):

        qp = self.painter
        qp.begin(self)
        self.drawEcosysteme(qp)
        qp.end()
    # --------------------------------------------    
    def drawEcosysteme(self, qp):
        
        qp.setPen(QtCore.Qt.red)
        for ins in self.ecosys:
             # qp.drawEllipse(ins.x,ins.y, 10,5)  
             if ins.car() == 'F' :
               qp.setPen(QtCore.Qt.green)
               qp.drawRect(ins.x,ins.y, 10,5)
             else:
               qp.setPen(QtCore.Qt.red)
               qp.drawEllipse(ins.x,ins.y, 10,5)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
    
