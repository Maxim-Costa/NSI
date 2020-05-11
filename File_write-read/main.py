def Table(PathF):
    t = open(PathF, 'w')
    for i in range(2, 21):
        t.write("Table de multiplication de " + str(i) + " : \n")
        for j in range(21):
            t.write(str(i)+" fois "+str(j)+" vaut "+str(i*j) + '\n')
    t.close()


def getMax(pathF):
    t = open(pathF, 'r')
    f = t.readlines()
    maxi = f[0]
    for i in f:
        if len(i) > len(maxi):
            maxi = i
    print(maxi)
    t.close()


def FileCreate(PathF):
    import random
    alpha = [chr(i) for i in range(97, 123)]
    Number = [i for i in range(10)]
    t = open(PathF, 'w')
    for _ in range(500):
        name = random.choices(alpha, k=5)
        FirstName = random.choices(alpha, k=7)
        PhoneNumber = random.choices(Number, k=9)
        DateNai = str(random.randint(1, 31)) + "/" + \
            str(random.randint(1, 12)) + "/" + str(random.randint(1950, 2020))

        name = ''.join(map(str, name)).capitalize()
        FirstName = ''.join(map(str, FirstName)).capitalize()
        PhoneNumber = ''.join(map(str, PhoneNumber))

        t.write(name + " - " + FirstName + " - " +
                "0"+PhoneNumber + " - " + DateNai + '\n')
    t.close()


def DicoRepert(PathF):
    t = open(PathF, 'r')
    f = t.readlines()
    print(f)
    dico = {}
    for i in range(len(f)):
        l = f[i].split('-')
        dico[l[0]] = (l[1], l[2], l[3][:-2])
    for k, v in dico.items():
        print(k, ":", v)
    t.close()


FileCreate('repert.txt')
DicoRepert('repert.txt')
