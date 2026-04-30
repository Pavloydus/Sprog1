import math

class Zlomek:
    def __init__(self, citatel, jmenovatel):
        self.cita = citatel
        self.jmen = jmenovatel

    def __str__(self):
        return f"{self.cita}/{self.jmen}"
    
    def zkrat(self):
        gcd = math.gcd(abs(self.cita), abs(self.jmen))
        self.cita = int(self.cita / gcd)
        self.jmen = int(self.jmen / gcd)
        return self

    def __add__(self, jiny):
        novy_cita = self.cita * jiny.jmen + self.jmen * jiny.cita
        novy_jmen = self.cita * jiny.cita
        novy_zlom = Zlomek(novy_cita, novy_jmen)
        return novy_zlom.zkrat()
    
    def __eq__(self, jiny):
        if self.cita * jiny.jmen == self.jmen * jiny.cita:
            return True
        else:
            return False