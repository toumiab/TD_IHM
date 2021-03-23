# -*- coding: utf-8 -*-
"""
@author:TSAFACK
"""



import sys
from  Fenetre import *


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from Serveur import *



# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre 
# créée avec QT Designer. Nous configurons après l'interface utilisateur 
# dans le constructeur (la méthode init()) de notre classe



class MonAppli(QMainWindow,Ui_Form):
    
    
   def  __init__(self,url_dataBase):
       
     self.serveur= Serveur(url_dataBase)    
     QMainWindow.__init__(self)
        

     self.setupUi(self)
     
     self.show()
     

#==============================================================================
#   connexion entre composant graphiques et fonctions   
#==============================================================================

 

     self.timer1=QtCore.QTimer()
     
     QtCore.QObject.connect(self.timer1, QtCore.SIGNAL("timeout()"), self.mettre_ihm_a_jour)

     QtCore.SIGNAL("timeout()").connect(self.timer1, self.mettre_ihm_a_jour)

     self.timer1.start(3000)
     
     self.serveur.start()
     self.serveur.join()
     
 

#==============================================================================
#      gestion du graphique 
#==============================================================================

#       mise à jour des textes

#     self.label_infos_traitments.setText(self.serveur.__str__())
     self.label_data_base.setText("FireBase")     
     self.label_url_database.setText(self.serveur.url_database)


#     self.courbesTemps=self.matplotlibwidget.figure.add_axes([0.1,0.05, 0.8, 0.85])

    

 
     
   def quitter(self):
               
        print("fin")
        self.timer1.stop()

        self.close()
#        sys.exit()
             
   def mettre_ihm_a_jour(self):
       
        self.serveur.rechercherNouvelleImages()
#
#        if  not self.serveur.is_alive():
#            self.serveur.start()
#            self.serveur.join()
# 

       
        print("chemin "+self.serveur.donnees.chemin_derniere_image)
        
        self.label_temps_attente_valeur.setText(str(int(self.serveur.donnees.temps_d_attente))+'minute(s)')
        self.label_temps_de_traitement_valeur.setText(str(int(self.serveur.donnees.temps_de_traitement))+'seconde(s)')
        
        if len(self.serveur.donnees.liste_date) >0:
            
            self.label_data_derniere_image.setText(self.serveur.donnees.liste_date[-1])
        
        if self.serveur.donnees.chemin_derniere_image : 
            
            pixmap = QPixmap(self.serveur.donnees.chemin_derniere_image)
            self.label_image_traitee.setPixmap(pixmap)
        
         
#        if len(self.serveur.donnees.liste_date)>0:
#            
#            
#            print("courbe")    
#            self.courbesTemps.plot(self.serveur.donnees.liste_temps_d_attente)
#            
##            self.courbesTemps.xticks(range(len(data)), jours, rotation=45)
#            
#            
#            self.label_data_derniere_image.setText(str(self.serveur.donnees.liste_date[-1]))
#        
#        # on affiche l'image traitée
#        
#        self.matplotlibwidget.draw()    
        
if __name__ == "__main__":
    
    url_dataBase='https://multicamproject.firebaseio.com'
    app = QApplication(sys.argv)
    #Form = QtGui.QWidget()
    #ui = Ui_Form()
    #ui.setupUi(Form)
    Form=MonAppli(url_dataBase)
    app.lastWindowClosed.connect(Form.quitter)
    Form.show()
    sys.exit(app.exec_())