'''
Importování modulů v Pythonu

Větší programy je žádoucí členit do samostatných modulů.
Modul je soubor obsahující definice a příkazy v Pythonu.
Moduly v Pythonu jsou uloženy v samostatných souborech s příponou .py.
Definice uvnitř modulů mohou být importovány do jiných modulů nebo do interaktivní pythonovské konzoly.
Připojení modulů provádíme klíčovým slovem import.
'''

'''
Příklad importu modulu math. V tomto případě můžeme pomocí tečkového operátoru využít všechny atributy a funkce,
které nám modul math nabízí.
'''
import math
print(math.pi)
print('Goniometrické funkce: sin 45° = {}, cos 45° = {}'.format(math.sin(45), math.cos(45)))

'''
Příklad importu modulu sys a jedné jeho funkce path. Použijeme k tomu konstrukci:
from jméno_modulu import jméno_funkce
'''

from sys import path
print(path) # Zobrazuje seznam (list) cest k adresářům, které aplikace využívá

'''
Moduly math a sys patří k interním modulům, jež jsou součástí standardní instalace Pythonu.
Externí moduly jsou distribuovány systémem balíčků (packages) a musí být instalovány pomocí nástroje pip.

pip install <jméno_balíčku>

Balíček můžeme odinstalovat příkazem:

pip uninstall <jméno_balíčku>

Používáme-li virtuální prostředí (virtual environment), jsou nainstalované balíčky ukládány v adresáři tohoto prostředí
(v našem případě venv) v podsložkách Lib a site-packages.

Přehled všech instalovaných balíčků získáme příkazem:

pip list

Můžeme také vytvořit soubor requirements.txt, který obsahuje záznam všech tzv. závislostí naší aplikace - čili 
informace o všech balíčcích, které je nutné do virtuálního prostředí nainstalovat, aby aplikace mohla fungovat.
Vytvoření souboru requirements.txt provedeme příkazem:

pip freeze > requirements.txt

Zobrazení podrobnějších informací o některém z nainstalovaných balíčků získáme příkazem:

pip show <jméno_balíčku>

Automatickou instalaci všech závislostí zaznamenaných v souboru requirements.txt provedeme příkazem:

pip install -r requirements.txt     
'''

# V konzoli virtuálního prostředí proveďte instalaci externího balíčku camelcase
# (venv) E:\python\projekt\venv>pip install camelcase
# Poté tento balíček importujte
import camelcase
c = camelcase.CamelCase() # Konstruktor třídy CamelCase() vytvoří objekt v proměnné c
txt = 'ahoj světáku'
print(c.hump(txt)) # Metoda hump() přeformátuje předaný řetězec podle zásad camel syntaxe (velká první písmena slov)

"""
Cvičení 4:

Použijte vhodné moduly v Pythonu (včetně jejich případné instalace) k tomu, abyste: 
1) vypsali aktuální datum a čas
2) vypsali datum velikonoční neděle (easter) v následujících 5 letech
3) vypsali nejbližší rok, v němž bude Štědrý den v neděli

K řešení prvního úkolu je možné doporučit importovat interní modul datetime
Řešení dalších dvou úkolů můžete odvodit z příkladů v dokumentaci k externímu modulu dateutil - viz https://pypi.org/project/python-dateutil/
"""
import datetime
x = datetime.datetime.now()

print()
print("1.ukol")
print("---------------------------------")
print("Dnesni datum je:")
print(x.strftime("%I:%M:%S %p / %d.%B %Y"))
print("---------------------------------")
print()

"""
Výpočet Velikonoc

zdroj:https://cs.wikipedia.org/wiki/V%C3%BDpo%C4%8Det_data_Velikonoc#Metoda_v%C3%BDpo%C4%8Dtu

Chtěl jsem to udělat co nejpřesnější, tak jsem si raději našel přesný výpočet, s úplňkem, přestupným rokem atd. :

a = rok mod 19 (pozn.: po 19 letech se měsíční cyklus opakuje ve stejné dny)
b = rok mod 4 (pozn.: cyklus opakování přestupných roků)
c = rok mod 7 (pozn.: dorovnání dne v týdnu)
Pro 20. a 21. století platí konstanty:
m = 24
n = 5
d = (19a + m) mod 30
e = (n + 2b + 4c + 6d) mod 7
Den u a měsíc v Velikonoční neděle se určí následovně:

u = d + e − 9
Je-li u = 25, d = 28, e = 6 a a > 10, pak u = 18, v = 4 a Velikonoční neděle připadá na 18. duben.

Jinak, je-li u ≥ 1 a u ≤ 25, pak v = 4 a Velikonoční neděle připadá na u-tý duben.

Jinak, je-li u > 25, pak u = u − 7, v = 4 a Velikonoční neděle připadá na u-tý duben.

Jinak u = 22 + d + e, v = 3 a Velikonoční neděle připadá na u-tý březen.


"""





print("2. ukol")

print("---------------------------------")
print("Vypsani Velikonoci na dalsich 5 let, s vyuzitim datetime:")
print()
year = int(x.strftime("%Y"))
month = int(x.strftime("%m"))
for i in range(1, 7):
    a = year % 19
    b = year % 4
    c = year % 7

    m = 24
    n = 5
    d = (19 * a + m) % 30
    e = (n + (2 * b) + (4 * c) + (6 * d)) % 7

    u = d + e - 9


    if( u == 25 and d == 28 and e == 6 and a > 10):
        v = 4
        u = 18

    if( u >= 1 and u <= 25):
        v = 4

    if( u > 25 ):
        u -= 7
        v = 4

    else:
        u = (22 + d + e)
        v = 3
        q = v % 2

        if(u > 31):
            v += 1
            u = u - 31


    z = datetime.datetime(year,v,u)

    print(z.strftime("%d.%B %Y"))
    year += 1

print("---------------------------------")
from dateutil.rrule import *

today = datetime.datetime.now()

print()
print("3 . ukol")
print("---------------------------------")
year = rrule(YEARLY,dtstart=today,bymonth=12,bymonthday=24,byweekday=SU)[0].year
print("nejbližší rok, v němž bude Štědrý den v neděli je : %s" % year)
print("---------------------------------")
