CFG = [
    ['S', 'dB'],
    ['S', 'A'],
    ['A', 'd'],
    ['A', 'dS'],
    ['A', 'aBdB'],
    ['B', 'a'],
    ['B', 'aS'],
    ['B', 'AC'],
    ['D', 'AB'],
    ['C', 'bC'],
    ['C', 'ε'],
]

# function to check for whether a character is number or not
def isnumber(arg):
    switcher = {
        '0': True,
        '1': True,
        '2': True,
        '3': True,
        '4': True,
        '5': True,
        '6': True,
        '7': True,
        '8': True,
        '9': True,
    }
    return switcher.get(arg, False)


# an array which will carry the Context Free Grammar during operations
CNF = []

# function to display current array and derivation passed to it
def displayValues(values, derivation):
    print(derivation)
    for index, sublist in enumerate(values):
        print(index + 1, sublist[0], "->", sublist[1])


# function to remove ε from CFG
def eliminatingEpsilon(CFG):
    emptyLetters = [] # non-symbol symbol whic derives in ε
    # Removing ε
    for index, sublist in enumerate(CFG):
        if "ε" in sublist[1]:
            # taking notes of which value is ε
            emptyLetters.append(sublist[0])
        else:
            CNF.append(CFG[index])

    # to add all the new links
    for val in CNF:
        for symbol in emptyLetters:
            tempVal = val[1]
            # replace one by one all empty letters if found to generate new rules
            while symbol in tempVal:
                tempVal = tempVal.replace(symbol, "") # deletes the symbol 
                CNF.append([val[0], tempVal])

    flag = False 
    for i, val in enumerate(CNF):
        # if string's length is 0, then adds ε and repeats the function, flag = true
        if len(val[1]) == 0:
            CNF[i][1] = "ε"
            flag = True

    if flag:
        eliminatingEpsilon(CFG)


def eleminatingRenamings(CNF):
    # remove all letters with self loop
    renamingRules = [] 
    for index, item in enumerate(CNF):
        if len(item[1]) == 1 and item[1].upper() == item[1]: # if string's length is 1 and is uppercase letter 
            renamingRules.append(CNF.pop(index)) # adds ['S', 'A'] and ['B', 'A']

    list = []
    for x in CNF:
        for y in renamingRules:
            if x[0] == y[1]:
                list.append([y[0], x[1]]) # output :[['S', 'd'], ['B', 'd'], ['S', 'dS'], ['B', 'dS'], ['S', 'aBdB'], ['B', 'aBdB']]

    for element in list:
        CNF.append(element)
    pass


def eliminatingInaccessibleSymbols(CNF, Starts, startlen):
    removed = []
    # finding all inaccessible elements
    for index, item in enumerate(CNF):
        if item[0] not in Starts: 
            removed.append(CNF.pop(index))
            for ch in item[1]:
                if ch.isupper() and not ch in Starts:
                    Starts.append(ch)
        else:
            for ch in item[1]:
                if ch.isupper() and not ch in Starts:
                    Starts.append(ch)
  

    # removing all inaccessible elements
    for rm in removed:
        if rm[0] in Starts:
            CNF.append(rm)
    if not len(Starts) == startlen:
        eliminatingInaccessibleSymbols(CNF, Starts, len(Starts))
    pass


def eliminatingNonproductiveSymbols(CNF):
    useless = []
    nonTerminal = []
    # getting all the non-symbol symbols with only one condition and containing a self loop
    for index, item in enumerate(CNF):
        if item[0] not in nonTerminal:
            nonTerminal.append(item[0]) # adds S, A, B , C, D
    for symbol in nonTerminal:
        flag = True
        for item in CNF:
            if item[0] == symbol: # searching for self loop
                if len([x for x in item[1] if(x == symbol)]) < 1:
                    flag = False
        if flag:
            useless.append(symbol)
    # removing those elements
    for opt in useless: # removes all production related to useless symbol
        for index, item in enumerate(CNF):
            if opt in item[0] or opt in item[1]:
                CNF.pop(index)
    pass


def convertToCNF(CNF):
    symbols = []
    symbolsNotation = []
    nonsymbols = []
    # Changing all non single digit symbol values to non symbol X1,X2 and so on
    for index, elem in enumerate(CNF):
        arr = [x for x in elem[1] if x.islower()] # a , b , d
        if len(arr) > 0:
            for item in arr:
                if item not in symbols:
                    symbols.append(item)
                    symbolsNotation.append(
                        [f"X{len(symbolsNotation)+1}", item])
                    if len(CNF[index][1]) > 1:
                        CNF[index][1] = CNF[index][1].replace(
                            item, f"X{len(symbolsNotation)}")
                else:
                    for lcaseValues in symbolsNotation:
                        if len(CNF[index][1]) > 1:
                            CNF[index][1] = CNF[index][1].replace(
                                lcaseValues[1], lcaseValues[0])

    # Since in previous step removed all symbol variables now just replacing more than 2 digit long non symbol variable by spliting last variable out
    # giveing rest of varable name with Y and also appending Y's value at the end
    for index, elem in enumerate(CNF):
        if len(elem[1]) >= 3:
            if len(elem[1]) == 3 and "X" in elem[1]:
                pass
            else:
                tex = elem[1]
                if isnumber(elem[1][-1]):
                    exceptLast = tex[:-2]
                    last = tex[-2:]
                else:
                    exceptLast = tex[:-1]
                    last = tex[-1:]
                if exceptLast not in nonsymbols:
                    nonsymbols.append(exceptLast)
                    CNF[index][1] = f"Y{len(nonsymbols)}{last}"
                    CNF.append([f"Y{len(nonsymbols) }", f"{exceptLast}"])
                else:
                    CNF[index][1] = f"Y{nonsymbols.index(exceptLast) + 1}{last}"
    for item in symbolsNotation:
        CNF.append(item)

    newCNF = []

    for item in CNF:
        if item not in newCNF:
            newCNF.append(item)

    return newCNF
    pass


displayValues(CFG, "Step 0: Orignal CFG")

eliminatingEpsilon(CFG)
displayValues(CNF, "Step 1: ε Removed from CFG")

eleminatingRenamings(CNF)
displayValues(CNF, "Step 2: Elimination of renamings")

eliminatingNonproductiveSymbols(CNF)
displayValues(CNF, "Step 3: Elimination of non productive symbols")

eliminatingInaccessibleSymbols(CNF, ["S"], 1)
displayValues(CNF, "Step 4: Removal of  inaccessible symbols")

newCNF = convertToCNF(CNF)
displayValues(newCNF, "Step 5: Chomsky Normal Form ")