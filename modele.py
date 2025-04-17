import random #pour la classe modele same


class Case:


    #dictionnaire avec les billes de couleurs :
    COLORS = {
        "bleu": 0,
        "vert": 1,
        "orange": 2,
        "vide": -1
    }
    
    def __init__(self, couleur):
        self._couleur = couleur
        if couleur == Case.COLORS["vide"]: #modif 2 : couleur d'une case vide
            self._compo = 0 #pcq une case vide n'appartient à aucune composante
        else:
            self._compo = -1 #case nn vide pas encore affecté à une composante


#retourne la couleur de la bille :
    def couleur(self):
        return self._couleur

#change la couleur de la bille :
    def change_couleur(self, nouvelle_couleur): #on va pouvoir l'appeler plusieurs fois au cours du jeu
        self._couleur = nouvelle_couleur
        if nouvelle_couleur == Case.COLORS["vide"]: #modif 2
            self._compo = 0 #si la case est vide, aucune compo
        else :
            self._compo = -1 #nouvelle couleur 


    def supprime(self): #enleve la bille de la case
        self._couleur = Case.COLORS["vide"]
        self._compo = 0 #modif 2

    def est_vide(self): #si la case est vide
        return self._couleur == Case.COLORS["vide"] 
    


    
    #nouvelle méthode de l'étape 2 :

    def composante (self) : #retourne le numéro de la composante
        return self._compo
    
    def pose_composante (self,num:int) : #num entier qui est affecté comme num. de composante pour le case
        self._compo = num
    
    def supprime_compo (self): #désaffecte un num de composante à la case (-1) si vide -> 0
        if self.est_vide():
            self._compo = 0
        else:
            self._compo = -1

    def parcourue (self): #teste si la case a été affectée à un numéro de composante
        return self._compo != -1 #pcq -1 désigne une case nn explorée par l'algo donc ça dois etre différent d'où le principe de la fonction





################################################################


class ModeleSame:

    def __init__(self,nblig=15,nbcol=20,nbcouleurs=3):
        self._nblig = nblig
        self._nbcol = nbcol
        self._nbcouleurs = nbcouleurs
        #init la grille de bille, à savoir liste de ligne (boucle extérieur) et chaque ligne possède des objets dans Case avec une couleur aléatoire entre 0 et nbcouleur-1 :
        self.mat = [[Case(random.randint(0, self._nbcouleurs - 1)) for _ in range(self._nbcol)]for _ in range(self._nblig)]
        self.nb_elts_compo = []
        self.score = 0
        self.calcule_composantes()


    def nblig(self): #accéder au lig
        return self._nblig

    def nbcol(self): #accéder au col
        return self._nbcol

    def nbcouleurs(self):
        return self._nbcouleurs
    
    def coords_valides(self,i,j): #vérifier si les coordonnées (i,j) sont bien intrèque
     if 0 <= i < self._nblig and 0 <= j < self._nbcol:
         return True
     else:
        return False

    def couleur(self,i,j): #retourne la couleur en coord
        if self.coords_valides(i,j): #on vérifie qu'elle est bien dans la grille
            return self.mat[i][j].couleur()
        else:
            return None

    def supprime_bille (self,i,j): #supprime la bille en 1 coordonée
        if self.coords_valides(i,j): #on vérifie qu'elle est bien dans la grille
            self.mat[i][j].supprime()


#reintialise tt les cases en changeant leur couleur :
    def nouvelle_partie (self): 
        for i in range(self._nblig): #parcourt les lig
            for j in range(self._nbcol): # pr chaque lig on parcourt les col
                nouvelle_couleur = random.randint(0, self._nbcouleurs-1) #on choisit aléatoirement soit bleu/vert/rouge
                self.mat[i][j].change_couleur(nouvelle_couleur) #on lui attribue sa nouvelle couleur
        self.calcule_composantes() 




#nouvelle méthode etape 2 : 


#renvoie la composante de la bille en (i,j)
    def composante (self, i,j) :
        if self.coords_valides(i, j): #on vérifie qu'elle est bien dans la grille
            return self.mat[i][j].composante()
        else:
            return None
        
#etape 4 

    def cases_composante(self, num):
        """Renvoie la liste des coordonnées (i,j) de la composante numéro `num`."""
        cases = []
        for i in range(self._nblig):
            for j in range(self._nbcol):
                if self.mat[i][j].composante() == num:
                    cases.append((i, j))
        return cases



    def calcule_composantes(self):
        self.nb_elts_compo = [0] #init à 0 (case vide)
        num_compo = 1 #init à 1
        for i in range(self._nblig): # on parcourt tt les lig de la matrice
            for j in range(self._nbcol): # on parcourt tt les col de la matrice
              if self.mat[i][j].composante() == -1: #on regarde que les cases de la mat qui sont colorés
                    couleur = self.mat[i][j].couleur()
                    taille = self.calcule_composante_numero(i, j, num_compo, couleur)
                    self.nb_elts_compo.append(taille)
                    num_compo += 1

    



    def calcule_composante_numero(self, i, j, num_compo, couleur): #méthode recursive
        if not self.coords_valides(i, j): #si les coordonnées ne sont pas valide on exclue 
          return 0
        case = self.mat[i][j] #on veut la case qui se trouve en (i,j) pour la manipuler

        if case.couleur() != couleur or case.parcourue(): #2 cas qu'on exclue de nouveau à savoir si la case ne possède pas la bonne couleur ou alors on l'a déjà parcourue
            return 0
        
        case.pose_composante(num_compo)
        taille = 1
        #récursivité on va rappeler notre fonction :
        droite = self.calcule_composante_numero(i, j + 1, num_compo, couleur)
        gauche = self.calcule_composante_numero(i, j - 1, num_compo, couleur)
        haut = self.calcule_composante_numero(i - 1, j, num_compo, couleur)
        bas = self.calcule_composante_numero(i + 1, j, num_compo, couleur)
        taille = taille + droite + gauche + haut + bas
        return taille



    def recalc_composantes(self): #lancer le calcul des composantes
        for i in range(self._nblig):
            for j in range(self._nbcol):
              self.mat[i][j].supprime_compo()
        self.calcule_composantes()


    def supprime_composante(self, num_compo):
        if num_compo <= 0 or num_compo >= len(self.nb_elts_compo):
            return False
        nb = self.nb_elts_compo[num_compo]
        if nb < 2:
            return False
        # modification etape3
        #afin d'appeler la fonction fonction suppprime_colonnes_vides
        for j in range(self._nbcol):
        #on veut qu'elle appelle suprime_composante_colonne
            self.supprime_composante_colonne(j, num_compo)
        self.supprime_colonnes_vides()
        gain = (nb-2) * (nb-2)
        self.score = self.score + gain
        self.recalc_composantes()
        return True



#nouvelle méthode etape 3 : 

    def est_vide (self, i ,j): #renvoie si la case est vide en (i,j)
        return self.mat[i][j] == None
    
    def supprime_composante_colonne (self, j, num_compo): #supprime les billes de la composante num_compo qui se trouve dans la colonne j
        colonne_filtrée = []
        for i in range(self._nblig):
            case = self.mat[i][j]
            if case.composante() != num_compo:
                colonne_filtrée.append(case)
        nb_vide = self._nblig - len(colonne_filtrée)
        colonne_filtrée = [Case(Case.COLORS["vide"]) for _ in range(nb_vide)] + colonne_filtrée
        for i in range(self._nblig):
            self.mat[i][j] = colonne_filtrée[i]

    def supprime_colonnes_vides (self): #décale les colonnes vers la droite de la matrice
        colonnes_denses = []
        for j in range(self._nbcol):
            est_vide = True
            for i in range(self._nblig):
                if not self.mat[i][j].est_vide():
                    est_vide = False
                    break
            if not est_vide:
                colonne = [self.mat[i][j] for i in range(self._nblig)]
                colonnes_denses.append(colonne)
        nb_vides = self._nbcol - len(colonnes_denses)
        for _ in range(nb_vides):
            colonnes_denses.append([Case(Case.COLORS["vide"]) for _ in range(self._nblig)])
        for j in range(self._nbcol):
            for i in range(self._nblig):
                self.mat[i][j] = colonnes_denses[j][i]




