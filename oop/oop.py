class Hrac:
    #konstruktor
    def __init__(self,name):
        #attributy
        self.jmeno = name
        self.hp = 100
        self.__money = 20
    #metody
    def zraneni(self, dmg):
        self.hp -= dmg
    def money_check(self):
        vysledek = self.__money
        print(vysledek)

hrac1 = Hrac("David")
print(hrac1.hp)
hrac1.zraneni(20)
print(hrac1.hp)
hrac1.money_check()