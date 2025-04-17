# tester mon code via le terminal

from modele import Case, ModeleSame  #Importation

case1 = Case(Case.COLORS["bleu"])
print(case1.couleur())  #0

case1.change_couleur(Case.COLORS["rouge"])
print(case1.couleur())  #2

case1.supprime()
print(case1.est_vide())  #True

case2 = Case(Case.COLORS["vide"])
print(case2.est_vide())  #True

#######

modele = ModeleSame()
print(modele.nblig())  #15
print(modele.nbcol())  #20
print(modele.nbcouleurs())  #4

print(modele.couleur(0, 0))  #aléa

modele.supprime_bille(0, 0)
print(modele.mat[0][0].est_vide())  #True

modele.nouvelle_partie()
print(modele.couleur(0, 0))  #aléa