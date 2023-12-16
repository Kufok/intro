from ast import Break

import random

def pozdrav(pocet_pozdravu):
    print("Ahoj " * int(pocet_pozdravu))

vec = "auto " # str

cislo = 7  # int

nahodne_cislo = random.randint(1, 100)

print("kolikrat te mam pozdravit?")

pocet_pozdravu = input()

pozdrav(pocet_pozdravu)

print(vec + str(cislo) + " Napis jsem neco") # napise neco

uzivatele_input =  input () # vezme neco

print("napsal jsi " + uzivatele_input) # vzal neco a spolil to

print("vybral jsem ti cislo " + str(nahodne_cislo)) # nahodne cilso

if nahodne_cislo > 10: # jestli neco je
    print("Tvoje cislo je vetsi nez 10")

print("Napis jsem neco")

uzivatele_vec = input()

while True:
    if uzivatele_vec.isnumeric():
        print("Napsal jsi cislo")
        break
    else:
        print("Napsal jsi text")
        break

print("ahoj")