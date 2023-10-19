class konyvek():
	cim = szerzo = isbn=""
	darab = 0
	
	def filldata(self):
		cim=input("Adja meg a címet:\n")
		cim=input("Adja meg a szerzőt:\n")

konyvpl=konyvek() #példány

konyvpl.filldata()