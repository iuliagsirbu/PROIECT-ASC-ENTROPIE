import math
import ast

def reset():
    f = open("cuvinte.txt", "r")
    
    dict = {}
    list = []
    suma = {}

    for x in f: #aici formez fiecare litera si frecv ei, alaturi de frecv fiecarei pozitii a ei
        list = []
        for i in range(5):
            if x[i] in dict:
                list = dict[x[i]]
                list[i] += 1
                dict[x[i]] = list
            else:
                #print(i)
                dict[x[i]] = [0, 0, 0, 0, 0]
                list = dict[x[i]]
                list[i] = 1
                dict[x[i]] = list

    dict = {key: value for key, value in sorted(dict.items())}

    with open("test.txt", 'w') as g:
        print(dict, file = g)
        """for key, value in dict.items():
            g.write('%s:%s\n' % (key, value)) #scriu in test.txt dictionarul"""

    for x in dict:   #aparitiile totale ale fiecarei litere, indiferent de pozitia ei
        suma[x] = sum(dict[x])


    formula = 0
    entropie = {}

    f.seek(0)  #resetez fisierul pentru a il putea citi din nou

    for x in f:   #calculez in dictionarul entropie formula de entropie pentru fiecare cuvant
        formula = 0
        for i in range(5):
            list = dict[x[i]]
            formula = formula + (list[i]/suma[x[i]]) * math.log2(suma[x[i]] / list[i])
        entropie[x] = formula

    maxim = sorted(entropie.items(), key = lambda x:x[1], reverse = True) #preia dictionarul entropie si face o lista
    #cu ordinea cuvintelor descrescator in functie de entropie + entropia lor

    with open("entropiedescrescatoare.txt", "w") as h: #scrie in entropiedescrescatoare.txt cuv descrescator + entropia
        print(*maxim, sep = "\n" , file = h)

    with open("entropiacuv.txt", "w") as i: #scrie in entropiacuv.txt cuvintele alfabetic cu entropia lor
        for key, value in entropie.items():
            print(key, "  : ", value, file = i)

    with open("cuvordentropie.txt", "w") as j: #scrie in cuvordentropie.txt strict cuvintele descrescator in fct de entropie
        for x in maxim:
            print(x[0], sep = "\n", file = j)

def run():
    #from wordle import dicty

    with open("frecvactualizata.txt", "r") as l:
        data = l.read()
    dicty = ast.literal_eval(data)

    #print(dicty)

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
