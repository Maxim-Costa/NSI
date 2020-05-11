#!/usr/bin/python
# coding:utf-8

def fusion_champs(ch1,ch2):
  """
  Données : Question 1
             ch1 liste [str1,str2, int1]
             ch2 liste [str1,int2]  str1 et str1 sont les mêmes
  Resultat : Question2
  Mise à jour des champs
  """
  NvCh=[]
  for titre in ch1:
     NvCh.append(titre)  # Question 3
  NvCh.append(ch2[1])
  return NvCh



def fusion_tables(tab1,tab2):
  """
  Données : Question 4
          : tab1 liste de listes de type [str1,str2,int1]
          : tab2 liste de listes de type [str1,int2]
          str1 et str1 sont les mêmes chaine de caractère
  Résultat : Question 5
  """
  NvTab=[]
  for k in range(len(tab1)):
     NvTab.append(tab1[k])
     NvTab[k].append(tab2[k][1])  # Question 6
  print(f"NvTab == {NvTab}")
  return NvTab


fich1=open("MesNotes1.csv","r") #on ouvre en lecture le fichier occitanie.csv
champs1=fich1.readline() # champs prend pour valeur la première ligne 
lignes1=fich1.readlines() # lignes est une liste de chaines de caractères
fich1.close() # On ferme le fichier

fich2=open("MesNotes2.csv","r") #on ouvre en lecture le fichier occitanie.csv
champs2=fich2.readline() # champs prend pour valeur la première ligne 
lignes2=fich2.readlines() # lignes est une liste de chaines de caractères
fich2.close() # On ferme le fichier

# On crée les tables à l'aide d'une boucle et non par compréhension
table1=[]  # on initialise une table vide
ch1=champs1.rstrip().split(";")
for ligne in lignes1 : # On crée la table à l'aide d'une boucle
    liste=ligne.rstrip().split(";") #chaque item de lignes est converti en liste
    liste[2]=int(liste[2]) # on convertit au bon type
    table1.append(liste)  # on ajoute cette liste à la table

table2=[]  # on initialise une table vide               
ch2=champs2.rstrip().split(";")
for ligne in lignes2 : # On crée la table à l'aide d'une boucle
    liste=ligne.rstrip().split(";") #chaque item de lignes est converti en liste
    liste[1]=int(liste[1]) # on convertit au bon type
    table2.append(liste)  # on ajoute cette liste à la table


print(3*"\n")
print(ch1)
print(table1)
print(3*"\n")
print(ch2)
print(table2)

champs=fusion_champs(ch1,ch2)
table=fusion_tables(table1,table2)
print(3*"\n")
print(champs)
print(3*"\n")
print(table)

tri=sorted(table,key=lambda ligne: ligne[1],reverse=True)
print(tri)



print(3*"\n")
#def fusion(
