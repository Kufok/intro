print("Pri psani pismen pis velka")
print("Ahoj zahrajes si hru s moznostma")
print("Ocitl jses uprostred lesa")
print("A = Pujdes do jeskyne ")
print("B = Pujdes po strasidelne ceste ")
print("C = Pujdes za svetlem")
user_input = input()

if user_input == ("A"):
    print("Jsi v jeskyni kde litaji netopyri ale pak uslysis zvuk pujdes za nim")
    print("A = Ano")
    print("B = Ne")
    user_input_jeskyne = input()
    
    if user_input_jeskyne == ("A"):
        print("Sel jsi za zvukem kde jsi uvidel lva ktery te zabil")
        print("Prohral si")
    
    if user_input_jeskyne ==("B"):
        print("Jsi unaveny pujdes spat?")
        print("A = Ano")
        print("B = Ne")
        user_input_spanek = input()

        if user_input_spanek == ("A"):
            print("Ve spanku te zabil lev ktereho jsi slysel")
            print("Prohral si")
     
        if user_input_spanek == ("B"):
            print("V noci jses bal ale kdyz jsi uvidel lva tak jsi utekl a zachranil jses")
            print("Vyhral si")

elif user_input == ("B"):
    print("Vydal jses po strasidelne ceste kde jsi narazil na bazinu co udelas?")
    print("A = Vratis se")
    print("B = Zkusis jit do baziny a preplavat to")
    print("C = Vytahnes hulku a postavis most")
    user_input_cesta = input()
     
    if user_input_cesta == ("A"):
            print("Kdyz jses varcel tak te napadli banditi a zabili te")
            print("Prohral si")
     
    if user_input_cesta == ("B"):
         print("V bazine byl jozin z bazin a zabil te")
         print("Prohral si")
     
    if user_input_cesta == ("C"):
        print("Postavil si most pres ktery jsi presel cestou jsi podkal pani ktera prodavala koste za jeden zlatak. Koupis ho?")
        print("A = Ano")
        print("B = Ne")
        user_input_koste = input()
        
        if user_input_koste == ("A"):
             print("Odletl si")
             print("Vyhral si")
    
        if user_input_koste == ("B"):
            print("Prosel si kolem ale cestou te prepadli banditi a zabili te")
            print("Prohral si")

elif user_input == ("C"):
    print("Sel jsi za svetelem, vydel jsi dum, zatukal si na dvere a stara pani ti otevrela, ty si vesel dovnitr a ptala se te jesstli neco nechces?")
    print("A = Ano")
    print("B = Ne")
    user_input_svetlo = input()

    if user_input_svetlo == ("A"):
        print("Pani ti priesla jidlo ty si ochutnal ale jidlo bylo otravene a umrel jsi")
        print("Prohral jsi")
        
    if user_input_svetlo == ("B"):
        print("Pani ti rekla aby si prespal. Prespis?")
        print("A = Ano")
        print("B = Ne")
        user_input_perespat = input()

        if user_input_perespat == ("A"):
            print("Pani te zabila ve spnaku")
            print("Prohral jsi")

        if user_input_perespat == ("B"):
            print("Prezil jsi")
            print("Vyhral jsi")

else:
    print("Takova moznost neexistuje")

    