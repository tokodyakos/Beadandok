def ReadFromFile(filename):
    fopen = open(filename, 'r', encoding="UTF-8")
    readstr = fopen.read()
    fopen.close()
    return(readstr)

def readlnSFromFile(name):
    readlnslist = []
    fopen = open(name, 'r', encoding='UTF-8')
    readlnslist = fopen.readlines()
    fopen.close()
    return(readlnslist)

def changeAlphabet(lines,alpha):
    newlines = ""
    for w in lines:
        for i in range(len(w)):
            if w[i] == alpha:
                newlines += "*"
            else:
                newlines += w[i]
    return newlines

def writeToFile(name,lines_alpha):
    fopen = open(name, 'w', encoding='UTF-8')
    fopen.write(changeAlphabet(lines_alpha))
    fopen.close()

print(ReadFromFile(input("Adja meg a file nevét: ")))
words = readlnSFromFile(input("Adja meg a file nevét: "))
alphabet = input("Adja meg a cserélendő karaktert: ")
writeToFile("cserelt.txt", words, alphabet)