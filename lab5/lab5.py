class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        p = self.parent
        level = 0
        while p:
            level = level + 1
            p = p.parent
        return level

    def printTree(self):
        spaces = " " * self.getLevel() * 2
        spaces = spaces + "|__" if self.parent else ""
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.printTree()
        pass


Grammar = [
    ["S", "Ae"],
    ["A", "baB"],
    ["B", "Cd"],
    ["C", "D"],
    ["C", "CbD"],
    ["D", "c"]
]


string = "bacbcbcde"


first = {}
last = {}
actions = []
mydict = {}
precedence = []
prior = {}
tree = []


def getAllfirst(myelem, already=[]):
    mylist = []
    for elmt in mydict[myelem]:
        first = elmt[0]
        if not first in already:
            if first.isupper():
                already.append(first)
                mylist.append(first)
                mylist += getAllfirst(first, already)
            else:
                mylist += [first]
    return mylist


def getAllLast(myelem, already=[]):
    mylist = []
    for elmt in mydict[myelem]:
        for i, first in enumerate(elmt):
            if first.isupper() and not first in already:
                already.append(first)
                mylist += getAllLast(first, already)
            elif not first in already:
                already.append(first)
                mylist += [first]
    return mylist


def parseString(text, priority):
    allNodes = {}
    while(len(text) > 2):
        for elm in priority:
            if elm[1] in text:
                text = text.replace(elm[1], elm[0], 1)
                print(text, "  ", f"{elm[0]} --> {elm[1]}")
                flag = False
                for chr in elm[1]:
                    if chr.isupper() and chr in allNodes:
                        flag = True

                if not flag:
                    node = TreeNode(elm[1])
                    parentNode = TreeNode(elm[0])
                    parentNode.add_child(node)
                    allNodes[elm[0]] = parentNode
                else:
                    parentNode = TreeNode(elm[0])
                    for chr in elm[1]:
                        if chr.isupper() and chr in allNodes:
                            parentNode.add_child(allNodes[chr])
                        else:
                            node = TreeNode(chr)
                            parentNode.add_child(node)

                    allNodes[elm[0]] = parentNode
    return parentNode


if __name__ == "__main__":

    # Converting array to dictionary
    for elm in Grammar:
        if elm[0] in mydict:
            mydict[elm[0]].append(elm[1])
        else:
            mydict[elm[0]] = [elm[1]]

    for elm in Grammar:
        myelem = elm[0]
        myelemFirst = elm[1][0]
        myelemLast = elm[1][1:]
        first[myelem] = getAllfirst(myelem, [])
        last[myelem] = getAllLast(myelem, [])

    # Assigning priority of all Staters/Nonterminal to 0
    for key in mydict:
        prior[key] = 0

    pr = []
    priority = []
    for el in Grammar:
        if len(el[1]) == 1 and el[1].islower():
            pr.append(el)

    StartingPoint = "S"
    el = mydict["S"][0]
    lowpr = []

    while not [StartingPoint, el] in pr:
        for elm in mydict[StartingPoint]:
            lowpr.append([StartingPoint, elm])
        for elm in mydict[StartingPoint]:
            for chr in elm:
                if chr.isupper():
                    el = mydict[chr][0]
                    StartingPoint = chr

    priority = pr

    for el in reversed(lowpr):
        priority.append(el)
    print(priority)

    root = parseString(string, priority)
    root.printTree()
