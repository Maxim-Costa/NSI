fich = open("C:/Users/theyk/OneDrive/Documents/NSI/TP_Tableau/france.csv", "r")
champs = fich.readline()
lignes = fich.readlines()
fich.close()

Newchamps = []
champs = champs.rstrip().split(";")

for i in lignes:
    ligne = i.rstrip().split(";")
    ligne[4] = int(ligne[4])
    ligne[5] = int(ligne[5])
    ligne[6] = float(ligne[6])
    Newchamps.append(ligne)


dept_plus = [i[1] for i in Newchamps if i[5] > 500000]
ma_selection = [[i[1], i[2], i[5], i[4]] for i in Newchamps if i[5] > 500000 and i[4] > 6000]
occitanie = [[i[0], i[1], i[3]] for i in Newchamps if i[2] == "Occitanie"]

