import ast
import program2
import matplotlib.pyplot as plt
import collections
BG_RED = "\u001b[41m"
BG_BBLUE = "\u001b[44;1m"
BG_YELLOW = "\u001b[43m"
BG_GRAY = "\u001b[48;5;240m"
BG_GREEN = "\u001b[42m"
RESET = "\u001b[0m"

plotvalues = {}

s = open("solutii.txt", "w")

with open("cuvinte_low.txt", "r") as c:
    for cuv in c:
        #print(cuv)
        program2.reset()

        guess = ""
        with open("cuvordentropie.txt", "r") as k:
            guess = k.readline()
        dicty = {}
        s.write(cuv +  ", ")
        print(f"{BG_BBLUE}{cuv}{RESET}", end= "")
        with open("test.txt", "r") as l:
            data = l.read()
        dicty = ast.literal_eval(data)

        nr_incercari = 0
        ok = 0

        if __name__ == "__main__":
            while ok==0:
                nr_incercari += 1
                #print("\n")
                #print("guess este ", guess, " dictionarul este ", dicty)
                ok2 = 1
                for i in range(5):
                    if guess[i] in cuv:
                        if cuv[i]==guess[i]:
                            s.write(cuv[i])
                            print(f"{BG_GREEN}{cuv[i]}{RESET}", end = "")
                            for x in dicty:
                                if x!=cuv[i]:
                                    list = dicty[x]
                                    list[i] = 0
                                    dicty[x] = list
                        elif cuv[i]!=guess[i]:
                            s.write(guess[i])
                            print(f"{BG_YELLOW}{guess[i]}{RESET}", end= "")
                            list = dicty[guess[i]]
                            list[i] = 0
                            dicty[guess[i]] = list
                    elif guess[i] not in cuv:
                        s.write(guess[i])
                        print(f"{BG_RED}{guess[i]}{RESET}", end ="")
                        for x in dicty:
                            if x == guess[i]:
                                list = dicty[x]
                                list = [0]*5
                                dicty[x] = list
                    with open("frecvactualizata.txt", "w") as v:
                            print(dicty, file = v)
                    program2.run()
                for i in range(5):
                    if cuv[i]!=guess[i]:
                        ok2=0
                with open("cuvordentropie.txt", "r") as k:
                    guess = k.readline()
                if ok2 == 1:
                    ok = 1
                s.write(", ")
                print(end=", ")
            nr_incercari = nr_incercari - 1
            s.write(str(nr_incercari))
            if nr_incercari in plotvalues:
                plotvalues[nr_incercari] += 1
            else:
                plotvalues.update({nr_incercari: 1})
        s.write("\n")
        print("\n")
s.close()
nrghiciri = []
nrcuvinte = []
mean = 0
#print(plotvalues)
newplotvalues = collections.OrderedDict(sorted(plotvalues.items()))
plotvalues = newplotvalues
#print(plotvalues)
for key in plotvalues.keys():
    #print(key)
    nrghiciri.append(key)
    nrcuvinte.append(plotvalues[key])
for i in range(len(nrghiciri)):
    mean = mean + nrghiciri[i] * nrcuvinte[i]
mean = mean / sum(nrcuvinte)
plt.bar(range(len(plotvalues)), nrcuvinte, tick_label = nrghiciri)
plt.title(f"Numarul de incercari necesare este {mean}")
plt.show()