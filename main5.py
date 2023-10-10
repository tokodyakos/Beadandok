def napok_szama(honap1, nap1, honap2, nap2):
    if 1 <= honap1 <= 12 and 1 <= nap1 <= 31 and 1 <= honap2 <= 12 and 1 <= nap2 <= 31:
        napok1 = (honap1 - 1) * 31+ nap1
        napok2 = (honap2 - 1) * 31 + nap2
        eltelt_napok = napok2 - napok1
        
        if napok2 >= napok1:
            eltelt_napok = napok2- napok1
        
            return eltelt_napok
        else:
            return "A második dátumnak későbbinek kell lennie mint az első dátum."
    else:
        return "Hibás dátumok! Próbálja újra..."
honap1 = int(input("Adja meg az első hónapot: "))
nap1 = int(input("Adja meg az első napot: "))
honap2 = int(input("Adja meg a második hónapot: "))
nap2 = int(input("Adja meg a második napot: "))

eltelt_napok = napok_szama(honap1, nap1, honap2, nap2)
print(f"Eltelt napok száma: {eltelt_napok}")