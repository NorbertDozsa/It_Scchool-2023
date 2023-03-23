
    # 4 Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
    #  un singur agument reprezentand muchia cubului in metri.

                        # Formula:
                        #  V = L³

def get_volum_cub(muchia):
    v = muchia**3
    return v

    # 5. Scrieti o functie care returneaza volumul unui cilintru in litri,
    # Aceasta va primi doua argumente reprezentand inaltimea si raza bazei in metri.

                        # Formula:
                        #  V = pir**2h

PI = 3.14 

def get_volum_cilindru(height, r):
    v = PI*r**2*height
    return v

    # 6. Scrie o functie care converteste litrii in metri cubi.

def get_cubic_m(liters):
    m3 = liters / 1000
    return m3


#  7. Foloseste functiile de la pct. 4-6 pentru a calcula cate cuburi cu muchia de 18 metri
# sunt necesare pentru a umple un cilindru cu raza bazei de 20 m si inaltimea de 55 m.
# - Printeaza volumul cubului in metri cubi #### Volumul cubului: 20 m^3
# - Printeaza volumul cilindrului in metri cubi.
# - Printeaza rezultatul de la pct. 7
# - Toate valorile printate vor fi insotite de mesaje descriptive.


print(f"Volumul cubului cu michia de 18m este: {get_volum_cub(18)} m^3 ")
print(f"Volumul cilindrului cu raza 20m si inaltimea 55m este: {get_cubic_m(get_volum_cilindru(55, 20))} m^3")
