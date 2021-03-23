# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2017

@author: toumiab
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from interface import Ui_principale_ihm
from ecosysteme import Ecosysteme


# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre 
# créée avec QT Designer. Nous configurons après l'interface utilisateur 
# dans le constructeur (la méthode init()) de notre classe

class MonAppli(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # Configuration de l'interface utilisateur.
        self.ui = Ui_principale_ihm()
        self.ui.setupUi(self)
        # TO DO
#        palette = QtGui.QPalette()
#        pixmap = QtGui.QPixmap("arrierPlan.png")
#        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
#        self.setPalette(palette)
        self.painter= QtGui.QPainter()
        self.ui.conteneur.paintEvent=self.drawEcosysteme
        pal = QtGui.QPalette()
        pixmap = QtGui.QPixmap("arrierPlan.png")
        pal.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.ui.conteneur.lower()
        self.ui.conteneur.stackUnder(self)
        self.ui.conteneur.setAutoFillBackground(True)
        self.ui.conteneur.setPalette(pal)
        # modification de la taille de ta fenetre
  #      self.ui.conteneur.resize(500,400)
     
#        label = QtGui.QLabel(self)
#        # affichage de l'objet image dans le label
#        pixmap = QtGui.QPixmap("arrierPlan.png")
#        label.setPixmap(pixmap)
#        
#        # affichage du label au centre de la fenêtre
#        self.ui.conteneur.
#        

        y = self.ui.conteneur.height()
        x=  self.ui.conteneur.width()
        self.ecosys = Ecosysteme(60,150,x*y//20, x,y)
        # Connexion entre lles boutons et les méthodes
        self.ui.bouton_pas.clicked.connect(self.un_pas) 
        self.ui.bouton_gen.clicked.connect(self.generer) 
        self.ui.bouton_sim.clicked.connect(self.simuler)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.un_pas)
        
    def un_pas(self) :
#        print("un pas")
#        self.ecosys.unTour()
#        self.ui.centralwidget.update()
         if self.ecosys.nbtour > 0:
            print("Tourné")
            self.ecosys.unTour()
            self.ecosys.nbtour -= 1
            # self.ui.conteneur.update() # nécessaire pour la MAJ de l’IHM
         else:
             if self.timer.isActive :
                 self.timer.stop()
             QtWidgets.QMessageBox.question(self, 'Attention !',
                            'Le nombre de tours est épuisé',
                            QtWidgets.QMessageBox.Ok)
    def generer(self) :
        print("Genérer")
        self.ecosys=Ecosysteme(60,50,100, self.ui.conteneur.width(),self.ui.conteneur.height())
        # self.ui.conteneur.update()
    
#    def simuler(self):
#        print("Simuler")
#        self.ecosys.simuler()
#        self.ui.centralwidget.update()
            
    def simuler(self):
        self.timer.start(100)
    
        
    
#    def paintEvent(self, *args):
#
#        qp = self.painter
#        qp.begin(self.ui.conteneur)
#        
##        self.drawEcosysteme1(qp)
#        self.drawEcosysteme1(qp)
#        qp.end()
#        
    def drawEcosysteme(self,*arg):
        qp = self.painter
        qp.begin(self.ui.conteneur)
#        qp.setPen(QtCore.Qt.red)
        for ins in self.ecosys:
             # qp.drawEllipse(ins.x,ins.y, 10,5)  
             if ins.car() == 'F' :
               qp.setPen(QtCore.Qt.green)
               qp.drawRect(ins.x,ins.y, 10,5)
             else:
               qp.setPen(QtCore.Qt.red)
               qp.drawEllipse(ins.x,ins.y, 10,5)
        qp.end()
    def drawEcosysteme1(self, qp):
        
        for ins in self.ecosys:
#             ins.dessin(qp)  
#             self.ui.conteneur.setFocus(True)
             ins.dessinimage(qp)

    def drawEcosysteme2(self, qp):
        qp = self.painter
        qp.begin(self.ui.conteneur)
        for ins in self.ecosys:
#             ins.dessin(qp)  
#             self.ui.conteneur.setFocus(True)
             ins.dessinimage(qp)
        
        qp.end()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()

    window.show()
    app.exec_()
