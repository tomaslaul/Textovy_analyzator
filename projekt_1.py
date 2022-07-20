"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Laul
email: tomas.laul@me.com
discord: Tomáš#1025
"""

#hledani, syntaxe findall(pattern, string, flags=0)
from re import findall

#pocitadlo
from collections import Counter

#import zadani
from task_template import TEXTS
pocet_textu = len(TEXTS)

#znami uzivatele
uzivatele = {"bob": "123", "ann": "pass132", "mike": "password123", "liz": "pass123"}

# oddelovaci cara 
oddelovac = "-" * 41

#prihlaseni
print(oddelovac)
jmeno = input("username:")
heslo = input("password:")
uzivatel = (jmeno, heslo)
print(oddelovac)

#pokud je registrovany uzivatel
if uzivatel in uzivatele.items(): 
    print("Welcome to the app,", jmeno)
    print("We have", pocet_textu, "texts to be analyzed.")
    print(oddelovac)
    #volba textu
    volba = int(input("Enter a number btw. 1 and 3 to select: "))
    if volba == 0:
        print("wrong input, terminating the program..")
    elif volba <= pocet_textu:
        for index, text in enumerate(TEXTS, 1):
            if volba == index:
                # titlecase
                titlecase = (findall(r"\s([A-Z]\w+)", text))
                # uppercase
                uppercase = (findall(r"([A-Z][A-Z]+)", text))
                # lowercase
                lowercase = (findall(r"\s([a-z]+)", text))
                # numeric
                numeric = (findall(r"([0-9]+\s)", text))
                # sum
                total_sum = list(map(int, numeric))
                slova = (text.split())

                print(oddelovac)
                print("There are", len(slova), "words in the selected text.",)
                print("There are", len(titlecase), "titlecase words.",)
                print("There are", len(uppercase), "uppercsae words.",)
                print("There are", len(lowercase), "lowercase words",)
                print("There are", len(numeric), "numeric string",)
                print("The sum of all the numbers", (sum(total_sum)),)
                print(oddelovac)
                print("LEN| ", (3 * " "), "OCCURENCES", (3 * " "), "|NR.")
                print(oddelovac)
                 
                 # delka
                sumar_slov = [] 
                for pozice, slovo in enumerate(slova, 1):
                    sumar_slov.append(len(slovo))
                cislo = range(1, len(sumar_slov))
                cisla = []
                for (cislo) in sorted(sumar_slov):
                    cisla.append(cislo)
                delky_slov = Counter(cisla)
                for key, value in sorted(delky_slov.items()):
                    print(f"{key: >3} | {('*' * value): <18} | {value}") 
                break
    else:
        print("wrong input, terminating the program..")

else:
    print("unregistered user, terminating the program..")