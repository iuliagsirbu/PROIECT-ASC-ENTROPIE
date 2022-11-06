import ast
import program2
cuv = "ACASA"
guess = ""
with open("cuvordentropie.txt", "r") as k:
    guess = k.readline()
dicty = {}

with open("test.txt", "r") as l:
    data = l.read()
dicty = ast.literal_eval(data)

nr_incercari = 0
ok = 0

if __name__ == "__main__":
    while ok==0:
        nr_incercari += 1
        print("guess este ", guess, " dictionarul este ", dicty)
        ok2 = 1
        for i in range(5):
            if cuv[i] == guess[i]:
                for x in dicty:
                    if x!=cuv[i]:
                        list = dicty[x]
                        list[i] = 0
                        dicty[x] = list
            else:
                ok2 = 0
                for x in dicty:
                    if x == guess[i]:
                        list = dicty[x]
                        list[i]=0
                        dicty[x]=list
                with open("frecvactualizata.txt", "w") as v:
                    print(dicty, file = v)
                program2.run()
        with open("cuvordentropie.txt", "r") as k:
            guess = k.readline()
        if ok2 == 1:
            ok = 1
    print(nr_incercari)