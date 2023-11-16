from OOPkonyvtar import *

konyvtarpl = Konyvtar()
ans = input('Menü: q - kilépés,\n n - új könyv felvétele,\n'
            "f - könyv keresésem\n d - könyv törlése,\n"
            "l - könyvek listázása, s - adatbázis mentése\n")
while (ans!='q'):
    if(ans == 'n'):
        konyvtarpl.new_book()
    elif(ans == 'f'):
        konyvtarpl.find_book(input("Könyv neve:\n"))
    elif(ans == 'd'):
        konyvtarpl.del_book(input("Törlendő könyv neve:\n"))
    elif(ans == 'l'):
        konyvtarpl.list_books()
    elif(ans == 's'):
        konyvtarpl.save_books()
    else:
        print("Ilyen menüpont nincs...\n")
    ans = input('Menü: q - kilépés,\n n - új könyv felvétele,\n'
            "f - könyv keresése\n d - könyv törlése,\n"
            "l - könyvek listázása\n s - adatbázis mentése\n")