from time import *

class Konyv():
    book_data = []
    
    def filldata_konyv(self):
        act_data = []
        act_data = [input("Adja meg a könyvnek a címét:\n")]
        act_data = [input("Adja meg a könyvnek a szerzőjét:\n")]
        act_data = [input("Adja meg a könyvnek az ISBN számát:\n")]
        
        return act_data
    def __init__(self):
        self.book_data += self.filldata_konyv()

class Konyvtar(Konyv):
    place = []
    books = []
    printdata = ()
    
    def add_dict(self):
        elem = []   #Segéd váltózó az objektumon belül
        elem += [input("Adja meg a könyvtár nevét:\n")]
        elem += [input("Adja meg a könyvtár címét:\n")]
        
        self.place += [elem]
    
    def __init__(self):
        self.add_dict()
        self.printdata = ("Könyv címe:","Szerző:","ISBN:","Darab:")
    def new_book(self):
        elem = []   #Segéd lista
        dict_name=input("Adja meg a könyvtár nevét:\n")
        
        i = 0
        findel = 0
        while(i < len(self.place) and not (findel)):
            if(self.place[i][0] == dict_name):
                findel = 1
            i += 1
        if(not findel):
            print("A könvytár nem létezi az adatbázisban...\n")
            self.add_dict()
            
        elem += [dict_name]
        elem += [self.filldata_konyv]
        elem += [int(input("A könyv darabszáma:\n"))]
        
        self.books += [elem]
    def find_book(self, book_name):
        i = 0
        index = 0
        while(i < len(self.books) and index == -1):
            if (self.books[i][1][0] == book_name):
                index = i
                
                for k in range(len(self.books[i][1])):
                    print(self.printdata[k], self.books[i][1][0],"\n")
            i += 1
        if(index == -1):
            print("A könyv nem létezik az adatbázisban...\n")
            return -1
        else: return index
        
    def del_book(self, book_name):
        if(self.find_book(book_name) == -1):
            print("A(z)", book_name," könyv nincs az adatbázisban...")
        else:
                del self.books[self.find_book(book_name)]
        print(self.books)
    
    def list_books(self):
        for i in range(len(self.books)):
            for k in range(len(self.books[i][1])):
                print(self.printdata[k], self.books[i][1][k], "\n")
            print(self.printdata[-1], self.books[i][2], "\n")