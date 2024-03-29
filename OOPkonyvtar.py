from time import *

class Konyv():
    book_data=[]

    def filldata_konyv(self):
        act_data=[]
        act_data += [input("Adja meg a könyv címét:\n")]
        act_data += [input("Adja meg a könyv szerzőjét:\n")]
        act_data += [input("Adja meg az isbn számot:\n")]

        return act_data

    def __init__(self):
        self.book_data+=self.filldata_konyv()


class Konyvtar(Konyv):
    place=[]
    books=[]
    printdata=()

    def add_dict(self):
        elem = []
        elem += [input("Adja meg a könyvtár nevét:\n")]
        elem += [input("Adja meg a címet:\n")]

        self.place += [elem]

    def __init__(self):
        self.add_dict()
        self.printdata = ("Könyv címe:", "Szerző:", "ISBN:", "db:")

    def new_book(self):
        elem = []
        dict_name=input("Adja meg a könyvtár nevét:\n")
        i=0

        #print("Place:",self.place, dict_name,len(self.place))
        findel=0
        while( i<len(self.place) and not (findel) ):
            if self.place[i][0]==dict_name:
                findel=1
            i+=1

        if(not findel):
            print("A könyvtár nem létezik az adatbázisban.\n")
            self.add_dict()

        elem += [dict_name]
        elem += [self.filldata_konyv()]
        elem+= [int(input("A könyv darabszáma:\n"))]

        self.books+=[elem]

    def find_book(self,book_name):

        i = 0
        index=-1
        while (i < len(self.books) and index==-1):
            if self.books[i][1][0] == book_name:
                index=i

                for k in range(len(self.books[i][1])):
                    print(self.printdata[k],self.books[i][1][k],"\n")
            i += 1

        if (index==-1):
            print("A könyv nem létezik az adatbázisban.\n")
            return -1
        else:
            return index

    def del_book(self, book_name):
        if self.find_book(book_name)==-1:
            print("A(z) ",book_name," könyv nincs az adatbázisban!\n")
        else: #self.books[self.find_book(book_name)][1]=""
            del self.books[self.find_book(book_name)]

        print(self.books)

    def list_books(self):
        for i in range(len(self.books)):
            for k in range(len(self.books[i][1])):
                print(self.printdata[k], self.books[i][1][k], "\n")
            print(self.printdata[-1], self.books[i][2], "\n")

    def save_books(self):
        ido=localtime()
        name=""
        name+="savebooks"+str(ido[1])+str(ido[2])+str(ido[3])+".txt"
        fopen=open(name,'w')
        #print(self.books)
        for i in range(len(self.books)):
            for k in range(len(self.books[i][1])):
                fopen.write(self.printdata[k]+str(self.books[i][1][k])+"\n")
            fopen.write(self.printdata[-1]+ str(self.books[i][2])+ "\n")

        fopen.close()

konyvtarpl=Konyvtar()
ans=input("Menü: q - kilépés,\n n - új könyv felvétele,\n s - könyv keresése,\n d - könyv törlése,"
"\n l - könyvek listázása, s - adatbázis mentése\n")
while(ans!='q'):
    if(ans=='n'):
        konyvtarpl.new_book()
    elif(ans=='f'):
        konyvtarpl.find_book(input("Könyv neve:\n"))
    elif (ans == 'd'):
        konyvtarpl.del_book(input("Törlendő könyv neve:\n"))
    elif (ans== 'l'):
        konyvtarpl.list_books()
    elif(ans=='s'):
        konyvtarpl.save_books()

    else: print("Nincs ilyen menüpont\n")

    ans = input("Menü: q - kilépés,\n n - új könyv felvétele,\n f - könyv keresése,\n d - könyv"
"törlése,\n l - könyvek listázása, s - adatbázis mentése\n")