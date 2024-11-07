from varasto import Varasto

mehua = Varasto(100.0, name="Mehuvarasto")
olutta = Varasto(100.0, 20.2, name="Olutvarasto")

def init():
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def olut_getterit():
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehu_setterit():
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def ota(varasto: Varasto, maara: float, display: str):
    print(f"{varasto.name}: {varasto}")
    print(f"{display}.ota_varastosta({maara})")
    saatiin = varasto.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    print(f"{varasto.name}: {varasto}")

def lisaa(varasto: Varasto, maara: float, display: str):
    print(f"{varasto.name}: {varasto}")
    print(f"{display}.lisaa_varastoon({maara})")
    varasto.lisaa_varastoon(maara)
    print(f"{varasto.name}: {varasto}")

def virhe():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def main():
    init()

    olut_getterit()

    mehu_setterit()

    virhe()

    lisaa(olutta, 1000.0, "olutta")
    lisaa(mehua, -666.0, "mehua")

    ota(olutta, 1000.0, "olutta")
    ota(mehua, -32.9, "mehua")


if __name__ == "__main__":
    main()
