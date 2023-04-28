class Factura:      

    numar_curent = 1

    def __init__(self, valoare_totala) -> None:
        self.__number = Factura.numar_curent
        self.valoare_totala = valoare_totala
        Factura.numar_curent += 1


    @property
    def numar(self):
        return self.__number
        

f1 = Factura(100)
f2 = Factura(220)

print(f2.numar)