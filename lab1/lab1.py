Vn = ["S", "F", "L"]
Vt = ["a", "b", "c", "d"]
P = ["S->bS", "S->aF", "S->d&", "F->cF", "F->dF", "F->aL", "L->aL",
    "L->c&", "F->b&"]

adjList = {}

for rule in P:
    if rule[0] not in adjList.keys():
        adjList[rule[0]] = []
    a = [rule[3], rule[4]]
    adjList[rule[0]].append(a)

print(adjList)

word = input()
lengthWord = len(word)

flag = 0

def verify(edge, j):
    for a, b in edge:
        if word[j] == a:
            if b == '&' and j == (lengthWord - 1):
                flag = 1
                return flag
            else:
                return verify(adjList[b], j + 1)

if verify(adjList['S'], 0):
    print("String is accepted by FA")
else: 
    print("String is not accepted by FA")