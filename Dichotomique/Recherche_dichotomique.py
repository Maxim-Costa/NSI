def find_me(t, x):
    tr = False
    deb = 0
    fin = len(t)-1
    iteration = 0

    while not tr and deb <= fin:
        iteration += 1
        mil = int((deb+fin)/2)

        if t[mil] == x:
            tr = True
        else:
            if x > t[mil]:
                deb = mil + 1
            else:
                fin = mil - 1

    print(t[deb:fin+1])
    print("iteration : ", iteration)
    return tr


t = [i for i in range(1, 1000000)]
print("\n reponse : ", find_me(t, 1025))
