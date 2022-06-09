starts = []
Grammar = [
    ["S", "Ae"],
    ["A", "baB"],
    ["B", "Cd"],
    ["C", "D"],
    ["C", "CbD"],
    ["D", "c"]
]

string = "bacbcbcde"

mydict = {}
first = {}
last = {}
equal = []
lessthan = []
greaterthan = []


def getAllfirst(myelem, already="", upper=""):
    if myelem.isupper():
        if not myelem in upper:
            upper += myelem
            already += myelem
            if myelem in mydict:
                for elm in mydict[myelem]:
                    if not elm in upper and not elm in already:
                        first = elm[0]
                        already += "," + getAllfirst(first, "", upper)
                    else:
                        return ""
        else:
            return ""
    else:
        if not myelem in already:
            already += myelem
    return already


def getAllLast(myelem, already="", upper=""):
    if myelem.isupper():
        if not myelem in upper:
            upper += myelem
            already += myelem
            if myelem in mydict:
                for elm in mydict[myelem]:
                    if not elm in upper and not elm in already:
                        first = elm[-1]
                        already += "," + getAllfirst(first, "")
                    else:
                        return ""
        else:
            return ""
    else:
        if not myelem in already:
            already += myelem
    return already

# writes the string in the according way with signs 
def parse(string):
    string = "$" + string + "$"
    s = ""
    for i in range(len(string)-1):
        if [string[i], string[i+1]] in equal:
            s += "="+string[i+1]
        elif [string[i], string[i+1]] in lessthan or string[i] == "$":
            s += "<"+string[i+1]
        elif [string[i], string[i+1]] in greaterthan or string[i+1] == "$":
            s += ">"+string[i+1]
        else:
            s += string[i+1]
    s = "$"+ s
    return s

# for example CbD will be changed with C
def checkRule(param):
    for lists in Grammar:
        if param == lists[1]:
            return lists[0]
    pass

# checks for the <>, changes the start
def check(ss):
    flag = False
    start = -1
    end = -1
    for i in range(0, len(ss) - 1):
        if ss[i] == "<":
            flag = True
            start = i+1
        elif flag and ss[i] == ">":
            end = i
            flag = False
            break

    # puts = in the initially form like CbD, then changes it into C
    Replacerules = checkRule(ss[start:end].replace("=", ""))

    # write the form, but with no signs from the table
    ss = ss[:start] + Replacerules + ss[end:]
    return ss

# puts the signs in left and right from the table 
def rerule(ss):
    for i in range(0, len(ss) - 1):
        if ss[i] == "<" or ss[i] == ">" or ss[i] == "=":
            if not(ss[i-1] == "$" or ss[i+1] == "$"):
                a = "=" if [ss[i-1], ss[i+1]] in equal else ""
                b = "<" if [ss[i-1], ss[i+1]] in lessthan else ""
                c = ">" if [ss[i-1], ss[i+1]] in greaterthan else ""

                if len(a) > 0 and not ss[i] == "=":
                    ss = ss[:i] + a + ss[i + 1:]
                elif len(b) > 0 and not ss[i] == "<":
                    ss = ss[:i] + b + ss[i + 1:]
                elif len(c) > 0 and not ss[i] == ">":
                    ss = ss[:i] + c + ss[i + 1:]
    return ss


if __name__ == "__main__":
    # Converting array to dictionary
    letters = []
    for elm in Grammar:
        for el in [el for x in elm for el in x]:
            if not el in letters:
                letters.append(el)
        if not elm[0] in starts:
            starts.append(elm[0])
        if elm[0] in mydict:
            mydict[elm[0]].append(elm[1])
        else:
            mydict[elm[0]] = [elm[1]]

    # Sorting all Letters
    letters = sorted(letters)
    for i, l in enumerate(letters):
        if l == "S":
            s = letters.pop(i)
            letters.insert(0, s) #set S on 0 position, first
 

    for elm in Grammar:
        myelem = elm[0]
        myelemFirst = elm[1][0]
        myelemLast = elm[1][-1]
        first[myelem] = getAllfirst(myelemFirst, "")
        last[myelem] = getAllLast(myelemLast, "")

    print("\n \tFIRST\t\tLAST".expandtabs(10))
    for elm in starts:
        print(f"{elm}\t{first[elm]}\t\t{last[elm]}".expandtabs(10))

    print("\n")
    print("Rule1: X1", "=", "X2")
    for elm in mydict:
        for val in mydict[elm]:
            if len(val) > 1:
                for i in range(0, len(val)-1):
                    if not [val[i], val[i+1]] in equal:
                        equal.append([val[i], val[i+1]])
                        print(val[i], "=", val[i+1])

    print("\n")
    print("Rule2: X1", "<", "X2" )
    for elm in mydict:
        for val in mydict[elm]:
            if len(val) > 1:
                for i in range(0, len(val)-1):
                    if not [val[i], val[i+1]] in lessthan and val[i].islower() and val[i+1].isupper():
                        print(val[i], " <   First(", val[i+1], ") => {", first[val[i+1]].strip(), "}")
                        for el in first[val[i+1]].strip().split(","):
                            if len(el.strip()) > 0:
                                lessthan.append([val[i], el])

    print("\n")
    print("Rule3: X1", ">", "X2" )
    for elm in mydict:
        for val in mydict[elm]:
            if len(val) > 1:
                for i in range(0, len(val)-1):
                    if not [val[i], val[i+1]] in greaterthan and val[i].isupper() and val[i+1].islower():
                        print("Last(", val[i], ")  >  ", val[i+1], "=> {", last[val[i]].strip(), "}   >  ", val[i+1])
                        for el in last[val[i]].strip().split(","):
                            if len(el.strip()) > 0:
                                greaterthan.append([el, val[i+1]])

    table = {}
    letters.append("$")
    s = "   "
    for item in letters:
        s = s+item + "\t"
        for item2 in letters:
            table[item+item2] = "=" if [item, item2] in equal else "<" if [item, item2] in lessthan else ">" if [
                item, item2] in greaterthan else "<" if item == "$" else ">" if item2 == "$" else ""
            
    print("\n")
    print(s.expandtabs(6))

    for x, item in enumerate(letters):
        s = " "
        for y, item2 in enumerate(letters):
          s += table[item + item2] + "\t"
        print(item + s.expandtabs(6),"\n")
    print(f"String {string} \n")
    ss = parse(string)
    print(ss)
    parsedFlag = True
    for i in range(0, 100):
        ss = check(ss)
        ss = rerule(ss)
        print(ss)
        if ss == "$<S>$":
            print("\n","String is accepted")
            parsedFlag = False
            break
    if parsedFlag:
        print("The string is not accepted")
