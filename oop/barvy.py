class Color:
    def __init__(self, r, g, b):
        if r >= 0 and r <= 255:
            self.r = r
        if b >= 0 and b <= 255:
            self.b = b
        if g >= 0 and g <= 255:
            self.g = g
    
    def __str__(self):
        return str(f"RGB({self.r}, {self.g}, {self.b})")

    def __add__(self, jina):
        r = int(round((self.r + jina.r) / 2))
        g = int(round((self.g + jina.g) / 2))
        b = int(round((self.b + jina.b) / 2))
        return Color(r, g, b)
    
    def __mul__(self, nasobek):
        if nasobek >= 1:
            r = min(int(round(self.r * nasobek)), 255)
            g = min(int(round(self.g * nasobek)), 255)
            b = min(int(round(self.b * nasobek)), 255)
        else:
            r = max(int(round(self.r * nasobek)), 0)
            g = max(int(round(self.g * nasobek)), 0)
            b = max(int(round(self.b * nasobek)), 0)
        return Color(r, g, b)
    
    def invert(self):
        r = 255 - self.r
        g = 255 - self.g
        b = 255 - self.b
        return Color(r, g, b)
    
    def to_hex(self):
        hex_r = hex(self.r).removeprefix("0x")
        hex_g = hex(self.g).removeprefix("0x")
        hex_b = hex(self.b).removeprefix("0x")
        if len(hex_r) == 1:
            hex_r = "0" + hex_r
        if len(hex_g) == 1:
            hex_g = "0" + hex_g
        if len(hex_b) == 1:
            hex_b = "0" + hex_b
        return str(f"#{hex_r + hex_g + hex_b}").upper()

    def to_grayscale(self):
        #0.299 * r + 0.587 * g + 0.114 * b
        gr_r = int(round(0.299 * self.r))
        gr_g = int(round(0.587 * self.g))
        gr_b = int(round(0.114 * self.b))
        gray = gr_r + gr_g + gr_b
        return Color(gray, gray, gray)

   
"""red = Color(255, 0, 0)
blu = Color(0, 0, 255)
pur = Color(127, 0, 127)

print(red)
print(red + blu)
print(pur * 1.5)
print(pur * 0.5)
print(pur.invert())
print(pur.to_hex())
print(pur.to_grayscale())"""

cervena = Color(255, 0, 0)
zelena = Color(0, 255, 0)
modra = Color(0, 0, 255)
print(f"Červená: {cervena}")
print(f"Zelená: {zelena}")
print(f"Modrá: {modra}")
# Test 2: Míchání barev
fialova = cervena + modra
zluta = cervena + zelena
print(f"{cervena} + {modra} = {fialova}")
print(f"{cervena} + {zelena} = {zluta}")
# Test 3: Zjasňování/ztmavování
tmava_cervena = Color(100, 0, 0)
svetlejsi = tmava_cervena * 2
tmavsi = tmava_cervena * 0.5
print(f"{tmava_cervena} * 2 = {svetlejsi}")
print(f"{tmava_cervena} * 0.5 = {tmavsi}")
# Test 4: Inverze
oranzova = Color(255, 100, 0)
inv = oranzova.invert()
print(f"{oranzova} invertováno = {inv}")
# Test 5: Hex formát
print(f"{cervena} = {cervena.to_hex()}")
print(f"{oranzova} = {oranzova.to_hex()}")
# Test 6: Grayscale
barevna = Color(255, 100, 50)
seda = barevna.to_grayscale()
print(f"{barevna} -> šedá: {seda}")
# Test 7: Složitější výpočet
vysledek = (cervena + modra) * 1.5
print(f"({cervena} + {modra}) * 1.5 = {vysledek}")