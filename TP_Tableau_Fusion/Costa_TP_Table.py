#!/usr/bin/python
# coding:utf-8

def export(Model,table):
    """
    int = table est un dictionnaire
    out = file.csv sorted by moyenne 
    """
    NwTable = []
    for k,v in table.items():
        NwTable.append([k]+v)
    NwTable = sorted(NwTable,reverse=True,key=lambda colone: colone[-1])
    
    NwTable = [Model]+NwTable
    with open("./notes.csv","w+") as fp:
        for i in NwTable:
            fp.writelines(';'.join([str(x) for x in i])+";\n")

def fusion(table1,table2):
    """
    int = table1, table2 sont des dictionnaire
    out = fusion table1 et table2
    """
    NwDico = dict()
    for k in table1.keys():
        NwDico[k] = table1[k]+table2[k]
    return NwDico

def int_to_int(table):
    """
    int = table et une liste
    out = les intier de la liste sont des int
    """
    NwTable = []
    for i in table:
        try:
            NwTable.append(int(i))
        except:
            NwTable.append(i)
    return NwTable

def moyen(table, Model):
    """
    int = table1 est un dictionnaire
    out = add moyen note + model update
    """
    for k,v in table.items():
        TTnote = 0
        nbNote = 0
        for i in v:
            if isinstance(i, int):
                TTnote += i
                nbNote += 1
        moyenne = round(TTnote/nbNote,2)
        table[k] = v+[moyenne]

    Model.append("moyenne")
    return Model,table


with open("./notes1.csv", "r") as fp:
    ModelFichier1 = fp.readline().rstrip().split(";")
    Dico1 = dict()
    lignes1 = fp.readlines()
    for i in lignes1:
        TmpLigne = i.rstrip().split(";")
        Dico1[TmpLigne[0]] = int_to_int(TmpLigne[1:])


Model = ModelFichier1

with  open("./notes2.csv", "r") as fp:
    ModelFichier2 = fp.readline().rstrip().split(";")
    Dico2 = dict()
    lignes2 = fp.readlines()
    for i in lignes2:
        TmpLigne = i.rstrip().split(";")
        Dico2[TmpLigne[0]] = int_to_int(TmpLigne[1:])

Model += ModelFichier2[1:]

Dico = fusion(Dico1,Dico2)
print(Model)
print(Dico)
Model,Dico = moyen(Dico, Model)
print("\n")
print(Model)
print(Dico)
print("\n")
export(Model,Dico)
