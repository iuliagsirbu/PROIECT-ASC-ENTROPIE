import math

def run():
    from wordle import dicty
    with open("idk.txt", "w") as a:
        print(dicty, file = a)

    suma = {}
    for x in dicty:  # aparitiile totale ale fiecarei litere, indiferent de pozitia ei
        suma[x] = sum(dicty[x])
    #print("suma este", suma)

    formula = 0
    entropie = {}

    f = open("cuvinte.txt", "r")

    for x in f:  # calculez in dictionarul entropie formula de entropie pentru fiecare cuvant
        formula = 0
        for i in range(5):
            #print("x este ",x, " formula este ", formula)
            list = dicty[x[i]]
            if suma[x[i]] != 0 and list[i]!=0:
                if suma[x[i]] == list[i]:
                    formula += 1
                else:
                    formula = formula + (list[i] / suma[x[i]]) * math.log2(suma[x[i]] / list[i])
            else:
                formula = formula + 0
        entropie[x] = formula

    maxim = sorted(entropie.items(), key=lambda x: x[1], reverse=True)

    with open("entropiedescrescatoare.txt", "w") as h:
        print(*maxim, sep="\n", file=h)

    with open("entropiacuv.txt", "w") as i:
        for key, value in entropie.items():
            print(key, "  : ", value, file=i)

    with open("cuvordentropie.txt", "w") as j:
        for x in maxim:
            print(x[0], sep="\n", file=j)
