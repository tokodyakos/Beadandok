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
    def find_book(self,)