import ast
import program2
cuv = "SCOLI"
guess = "SCOLI"
dicty = {}

with open("test.txt", "r") as l:
    data = l.read()
dicty = ast.literal_eval(data)

for i in range(5):
    if cuv[i] == guess[i]:
        for x in dicty:
            if x!=cuv[i]:
                list = dicty[x]
                list[i] = 0
                dicty[x] = list
    if __name__ == "__main__":
        program2.run()