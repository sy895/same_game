from tkinter import Tk, Button, Label, PhotoImage
import os

"""Tk -> fenêtre
    Button -> pour les cases du jeu + le bouton 'au revoir' et 'nouveau'
    Label -> Score (texte statique)
    PhotoImage -> images des billes en .gif
    os -> chemin de fichier
"""

class VueSame:

    def __init__(self, modele):
        self.modele = modele
        self.fenetre = Tk()
        self.fenetre.title("Same Game")

        self.ecriture = ("Georgia", 14, "bold")  # ajout de la police élégante

        self.images = []  # toutes les images des billes
        self.images_noires = []  #etape 4 : images des billes en noir (survol)

        dossier_img = os.path.join("img")
        noms_img = [
            "tres_petit_sphere3.gif",
            "tres_petit_sphere6.gif",
            "tres_petit_sphere7.gif",
            "tres_petit_spherevide.gif"  # sphere vide à la fin
        ]

        for nom in noms_img:
            img = PhotoImage(file=os.path.join(dossier_img, nom))
            self.images.append(img)

            if "vide" not in nom:
                nom_noir = nom.replace(".gif", "black.gif")
                img_noir = PhotoImage(file=os.path.join(dossier_img, nom_noir))
            else:
                img_noir = img  # image vide reste identique

            self.images_noires.append(img_noir)

        self.__les_btns = []
        for i in range(self.modele.nblig()):
            ligne = []
            for j in range(self.modele.nbcol()):
                couleur = self.modele.couleur(i, j)
                bouton = Button(self.fenetre, image=self.images[couleur], command=self.creer_controleur_btn(i, j))
                bouton.grid(row=i, column=j)

                bouton.bind("<Enter>", self.creer_controleur_motion(i, j))  # survol
                bouton.bind("<Leave>", self.creer_controleur_leave(i, j))   # sortie

                ligne.append(bouton)
            self.__les_btns.append(ligne)

        self.label_score = Label(self.fenetre, text="Score : 0", font=self.ecriture)  # application police ici
        self.label_score.grid(row=self.modele.nblig() // 2 - 3, column=self.modele.nbcol() + 1)

        btn_nouveau = Button(self.fenetre, text="Nouveau", command=self.nouvelle_partie, font=self.ecriture)  # ici aussi
        btn_nouveau.grid(row=self.modele.nblig() // 2 - 1, column=self.modele.nbcol() + 1)

        btn_quitter = Button(self.fenetre, text="Au revoir", command=self.fenetre.quit, font=self.ecriture)  # idem
        btn_quitter.grid(row=self.modele.nblig() // 2 + 1, column=self.modele.nbcol() + 1)

        self.redessine()  # MAJ initiale
        self.fenetre.mainloop()  # dernière action du constructeur

    def creer_controleur_btn(self, i, j):  #retourne la fct
        def controleur_btn():  #demande au modele de supprimer la bille en (i,j)
            num = self.modele.composante(i, j)  #modif etape 2
            if self.modele.supprime_composante(num):  # ajout vérification suppression
                self.redessine()  # MAJ
        return controleur_btn

    def redessine(self):  #MAJ score
        for i in range(self.modele.nblig()):
            for j in range(self.modele.nbcol()):
                couleur = self.modele.couleur(i, j)
                self.__les_btns[i][j].config(image=self.images[couleur])

        self.label_score.config(text=f"Score : {self.modele.score}")


    def nouvelle_partie(self):
        self.modele.nouvelle_partie()
        self.redessine()

    def creer_controleur_motion(self, i, j):
        def handler(event):
            num = self.modele.composante(i, j)
            composante = self.modele.cases_composante(num)
            if len(composante) < 2:
                return
            for (x, y) in composante:
                couleur = self.modele.couleur(x, y)
                self.__les_btns[x][y].config(image=self.images_noires[couleur])
        return handler

    def creer_controleur_leave(self, i, j):
        def handler(event):
            num = self.modele.composante(i, j)
            composante = self.modele.cases_composante(num)
            if len(composante) < 2:
                return
            for (x, y) in composante:
                couleur = self.modele.couleur(x, y)
                self.__les_btns[x][y].config(image=self.images[couleur])
        return handler
