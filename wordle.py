import ast
import program2
BG_RED = "\u001b[41m"
BG_BBLUE = "\u001b[44;1m"
BG_YELLOW = "\u001b[43m"
BG_GRAY = "\u001b[48;5;240m"
BG_GREEN = "\u001b[42m"
RESET = "\u001b[0m"
cuv = "ACASA"
#cprint(cuv, 'red')
guess = ""
with open("cuvordentropie.txt", "r") as k:
    guess = k.readline()
dicty = {}
print(f"{BG_BBLUE}{cuv}{RESET}")
with open("test.txt", "r") as l:
    data = l.read()
dicty = ast.literal_eval(data)

nr_incercari = 0
ok = 0

if __name__ == "__main__":
    while ok==0:
        nr_incercari += 1
        print("\n")
        #print("guess este ", guess, " dictionarul este ", dicty)
        ok2 = 1
        for i in range(5):
            if cuv[i] == guess[i]:
                print(f"{BG_GREEN}{cuv[i]}{RESET}", end = "")
                for x in dicty:
                    if x!=cuv[i]:
                        list = dicty[x]
                        list[i] = 0
                        dicty[x] = list
            else:
                print(f"{BG_RED}{guess[i]}{RESET}", end = "")
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
    print("\n", nr_incercari)