'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.8 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 1080000000  #? rychlost světla ve vakuu
SPEED_OF_SOUND =1224  #? rychlost zvuku při teplotě 20 °C v suchém vzduchu
MOON = 384400 #? vzdálenost měsíce od naší planety

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
def gravity():
    '''
    Tato funkce zjišťuje gravitační sílu tělesa s ohledem k zemi
    '''
    print("-----------------------------GRAVITACNI SILA TELESA------------------------------")
    print("------------------------Za 1. zjisteni hmotnosti telesa--------------------------")
    hmotnost = input("Zadejte hmotnost telesa, ve formatu(5.12): ")
    print("---Zvolte si , jestli chcete vypocist g.silu vzhledem k mesici, nebo k zemi------")
    volba = input("1 = země, 2 = měsíc: ")
    if int(volba)==1:
         print("------------------------Gravitacni sila telesa na Zemi-----------------------")
         vypocet = float(EARTH_GRAVITY)*float(hmotnost)
         print(f'Vysledna gravitacni silan zemi je  {vypocet:8.2f}N\n')
    if int(volba)==2:
         print("------------------------Gravitacni sila telesa na Zemi-----------------------")
         vypocet = float(MOON_GRAVITY)*float(hmotnost)
         print(f'Vysledna gravitacni sila ne měsíci je  {vypocet:8.2f}N\n')
    else:
            print("------------------------Zadal/la jste spatnou hodnotu-----------------------")


def svetlozvuk():
    '''
    Tato funkce zjišťuje čas za jak dlouho dopadne zvuk, nebo svetlo ze zeme na mesic
    '''
    print("-----------------------------RYCHLOST ZVUKU A SVETLA------------------------------")
    print("--------------Zvolte si , jestli chcete vypocist cas zvuku, nebo svetla-----------")
    volba2 = input("1 = zvuk, 2 = svetlo: ")

    if int(volba2) == 1:
        print("--------------------------zvolil/la jste si zvuk----------------------------------")
        vypocet = float(MOON) * float(SPEED_OF_SOUND)
        print(f'Doba, kdy dopadne zvuk na mesic  {vypocet:8.2f}hodin\n')
        return
    if int(volba2) == 2:
        print("------------------------zvolil/la jste svetlo-----------------------")
        vypocet = float(MOON) * float(SPEED_OF_LIGHT)
        print(f'Doba, kdy dopadne svetlo ze zeme na mesic pri teplote 20 stupnu ;) {vypocet:8.2f}hodin\n')

    return


