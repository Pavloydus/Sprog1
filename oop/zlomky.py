import math

class Zlomek:
    def __init__(self, cit, jme = 1):
        self.cit = cit
        self.jme = jme

    def __str__(self):
        return f"{self.cit}/{self.jme}"
    
    def zkrat(self):
        gcd = math.gcd(abs(self.cit), abs(self.jme))
        self.cit = int(self.cit / gcd)
        self.jme = int(self.jme / gcd)
        return self
    
    def __add__(self, jiny):
        novy_cit = self.cit * jiny.jme + jiny.cit * self.jme
        novy_jme = self.jme * jiny.jme
        z = Zlomek(novy_cit, novy_jme)
        return z.zkrat()
    
    def __eq__(self, jiny):
        if self.cit * jiny.jme == jiny.cit * self.jme:
            return True
        else:
            return False
    
    def __lt__(self, jiny):
        if self.cit * jiny.jme < jiny.cit * self.jme:
            return True
        else:
            return False
        
    def to_float(self):
        return float(self.cit / self.jme)

        
z1 = Zlomek(2, 8)
z1.zkrat()
print(z1)

z2 = Zlomek(8, 2)
z3 = Zlomek(40, 3)
print(z2 + z3)
print(z2 < z3)

print(z3.to_float())