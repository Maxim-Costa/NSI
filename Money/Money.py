"""
rendu de money non optimiser
@Maxim_Costa 103
"""


def rendu(Argentdu, Piece):
    """
    input : Argentdu = int, Piece = list()
        L'argent du soit EURO plus CENTIME * 100, des intier || la liste des piece disponible (float('inf')) == infini format list de list [[Piece,nbPiece]]

    ouput : list de tuple [(Piece,nbPiece)] :
        le nombre de piece pour chaque piece qui sera rendu
    """
    if Argentdu == 0:
        return [[0]]
    elif Argentdu < 0:
        return [[Argentdu]]
    else:
        i = 0
        PieceRendu = []
        while Argentdu != 0:
            if Piece[i][1] > 0:
                x = Argentdu//Piece[i][0]
                if x != 0:
                    if x <= Piece[i][1]:
                        Argentdu -= x*Piece[i][0]
                    else:
                        Argentdu -= Piece[i][0]*Piece[i][1]
                        x = Piece[i][1]
                    Piece[i][1] -= x
                    PieceRendu.append((Piece[i][0], x))
            i += 1
        return PieceRendu


""" nombre de piece Centime et Euro,  float('inf') = infini"""
inf = float('inf')
Piece = [[200, inf],
         [100, inf],
         [50, inf],
         [20, inf],
         [10, inf],
         [5, inf],
         [2, inf],
         [1, inf]]


""" format euro.centime !! mettre un point et non une virgule """
PrixDepart = 3.09
ArgentDonner = 102.39

ArgentDonner *= 100
PrixDepart *= 100
Argent = ArgentDonner-PrixDepart


def printer(x):
    if x[0] > 0:
        if x[0] >= 100:
            print(
                f"{int(x[1])} piece{'s' if x[1]>1 else ''} de {int(x[0]/100)} Euro")
        else:
            print(
                f"{int(x[1])} piece{'s' if x[1]>1 else ''} de {x[0]} Centime")
    elif x[0] == 0:
        print("pas besoin de rendre")
    elif x[0] < 0:
        print(f"il manque de l'argent ({abs(x[0]/100)} Euro)")


list(map(lambda x: printer(x), rendu(Argent, Piece)))
