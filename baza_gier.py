import ast


menu = """
1. Wyświetl nazwy wszystkich gier w bazie
2. Wyświetl wszystkie gry w bazie
3. Wyświetl TOP 5 gier w bazie
4. Wyświetl gry z gatunku
5. Dodaj grę do bazy
6. Edytuj grę w bazie
7. Usuń grę z bazy
8. Wyświetl informacje o grze
9. Oceń grę
10. Zapisz dane do pliku
11. Odczytaj dane z pliku
12.Zakończ
"""
while True:

    baza_gier = [
        {"tytul": "Cyberpunk 2077", "rok_wydania": "2020", "gatunek": "RPG", "ocena_graczy": 2},
        {"tytul": "The Legend of Zelda: Breath of the Wild", "rok_wydania": "2017", "gatunek": "Przygodowa", "ocena_graczy": 3},
        {"tytul": "FIFA 22", "rok_wydania": "2021", "gatunek": "Sportowa", "ocena_graczy": 4},
        {"tytul": "Among Us", "rok_wydania": "2018", "gatunek": "Party", "ocena_graczy": 5},
        {"tytul": "Assassin's Creed Valhalla", "rok_wydania": "2020", "gatunek": "Akcja", "ocena_graczy": 11},
        {"tytul": "Minecraft", "rok_wydania": "2011", "gatunek": "Sandbox", "ocena_graczy": 10},
        {"tytul": "Fall Guys: Ultimate Knockout", "rok_wydania": "2020", "gatunek": "Battle Royale", "ocena_graczy": 9},
        {"tytul": "The Witcher 3: Wild Hunt", "rok_wydania": "2015", "gatunek": "RPG", "ocena_graczy": 8},
        {"tytul": "Super Mario Odyssey", "rok_wydania": "2017", "gatunek": "Platformer", "ocena_graczy": 7},
    ]

    wybor = input("Podaj opcje:  ")
    lista_wyborow = list( i for i in range(1,13))

    if not wybor.isnumeric() or int(wybor) not in lista_wyborow :
        continue
    else:
        wybor = int(wybor)
        if wybor == 1:
            posortowane_tytuly = sorted(baza_gier, key=lambda x: x["tytul"])

            for i in range(len(posortowane_tytuly)):
                for k,v in posortowane_tytuly[i].items():
                    if k == "tytul":
                        print(v)

            print(menu)
            wybor = input("Podaj opcje:  ")

        elif wybor == 2:
            posortowane_tytuly = sorted(baza_gier, key=lambda x: x["tytul"])

            for tytuly in posortowane_tytuly:
                print(tytuly)

            print(menu)
            wybor = input("Podaj opcje:  ")

        elif wybor == 3:
            posortowane_oceny = sorted(baza_gier, key=lambda x: x['ocena_graczy'])
            top_5 = posortowane_oceny[:3:-1]
            alfabetyczne_top_5 = sorted(top_5, key=lambda x:x["tytul"])
            print(alfabetyczne_top_5)

            print(menu)
            wybor = input("Podaj opcje:  ")

        elif wybor == 4:
            szukany_gatunek = input("Podaj gatunek szukanej gry: ")
            tytuly_szukanych_gatunkow = []
            for i in range(len(baza_gier)):
                baza = baza_gier[i]
                for k,v in baza.items():
                    if k == "gatunek" and v == szukany_gatunek:
                        tytuly_szukanych_gatunkow.append(baza)

            posortowane_tytuly_szukanych_gatunkow = sorted(tytuly_szukanych_gatunkow, key=lambda x: x["tytul"])
            for i in range(len(posortowane_tytuly_szukanych_gatunkow)):
                for k,v in posortowane_tytuly_szukanych_gatunkow[i].items():
                    if k == "tytul":
                        print(v)

        elif wybor == 5:
            tytul_do_dodania = input("Podaj tytul gry: ")
            while not tytul_do_dodania.isalpha():
                tytul_do_dodania = input("Podaj tytul gry: ")

            rok_wydania_do_dodania = input("Podaj rok_wydania gry: ")
            while not rok_wydania_do_dodania.isnumeric():
                rok_wydania_do_dodania = input("Podaj rok_wydania gry: ")

            gatunek_do_dodania = input("Podaj gatunek gry: ")
            while not gatunek_do_dodania.isalpha():
                gatunek_do_dodania = input("Podaj gatunek gry: ")

            domyslna_ocena_graczy = 0.0

            baza_gier.append({"tytul": {tytul_do_dodania}, "rok_wydania": {rok_wydania_do_dodania}, "gatunek": {gatunek_do_dodania}, "ocena_graczy": domyslna_ocena_graczy})
            print(baza_gier)
            print(menu)
            wybor = input("Podaj opcje:  ")

        elif wybor == 6:
            tytul_edytowanej_gry = input("Podaj tytul edytowanej gry: ")
            edytowana_gra = []
            for i in range(len(baza_gier)):
                baza = baza_gier[i]
                for k, v in baza.items():
                    if k == "tytul" and v == tytul_edytowanej_gry:
                        edytowana_gra.append(baza)
                    else:
                        print("Podana gra nie istnieje w bazie")
                        print(menu)
                        wybor = input("Podaj opcje:  ")

            tytul_do_dodania = edytowana_gra[0]["tytul"]
            ocena_graczy = edytowana_gra[0]["ocena_graczy"]
            while not tytul_do_dodania.isalpha():
                tytul_do_dodania = input("Podaj tytul gry: ")

            rok_wydania_do_dodania = input("Podaj rok_wydania gry: ")
            while not rok_wydania_do_dodania.isnumeric():
                rok_wydania_do_dodania = input("Podaj rok_wydania gry: ")

            gatunek_do_dodania = input("Podaj gatunek gry: ")
            while not gatunek_do_dodania.isalpha():
                gatunek_do_dodania = input("Podaj gatunek gry: ")



            nowa_gra = {"tytul": {tytul_do_dodania}, "rok_wydania": {rok_wydania_do_dodania}, "gatunek": {gatunek_do_dodania}}
            for gra in baza_gier:
                if gra[tytul_do_dodania] == edytowana_gra["tytul"]:
                    gra["rok_wydania"] = nowa_gra["rok_wydania"]
                    gra["gatunek"] = nowa_gra["gatunek"]

            print(baza_gier)
            print(menu)
            wybor = input("Podaj opcje:  ")
        elif wybor == 7:
            tytul_do_usuniecia = input("Podaj tytul gry do usuniecia z bazy: ")
            usuniety_element = None
            for i in range(len(baza_gier)):
                baza = baza_gier[i]
                for k, v in baza.items():
                    if k == "tytul" and v == tytul_do_usuniecia:
                        usuniety_element = baza
                        baza_gier.remove(usuniety_element)


            if usuniety_element == None:
                print("Nie ma takiego elementu w bazie ")
                continue



            print(menu)
            wybor = input("Podaj opcje:  ")

        elif wybor == 8:
            tytul_do_edycji = input("Podaj tytuł gry do wyświetlenia: ")
            czy_istnieje = False
            for i in range(len(baza_gier)):
                for k, v in baza_gier[i].items():
                    if k == "tytul" and v == tytul_do_edycji:
                        print(baza_gier[i])
                        czy_istnieje = True
                        break


            if not czy_istnieje:
                print("Nie ma takiego rekordu w bazie")
                continue


            print(menu)
        elif wybor == 9:

            tytul_do_edycji = input("Podaj tytuł gry do edycji: ")
            czy_istnieje = False
            for i in range(len(baza_gier)):
                for k, v in baza_gier[i].items():
                    if k == "tytul" and v == tytul_do_edycji:
                        czy_istnieje = True
                        break

            if not czy_istnieje:
                print("Nie ma takiego rekordu w bazie")
                continue
            else:

                nowa_ocena = input("Podaj ocenę: ")
                while not nowa_ocena.isnumeric():
                    nowa_ocena = input("Podaj ocenę: ")

            for gra in baza_gier:
                if gra["tytul"] == tytul_do_edycji:
                    gra["ocena_graczy"] = nowa_ocena
                    print("Edytowano pomyślnie")


            print(menu)
        elif wybor == 10:
            with open("gry.txt",'w') as plik:
                for i in range(len(baza_gier)):
                    plik.write(str(baza_gier[i]))
                    plik.write('\n')

            continue

        elif wybor == 11:

            if baza_gier:
                baza_gier.clear()
            with open("gry.txt", 'r') as plik:
                for x in plik:
                    baza_gier.append(x.strip())
            baza_gier = [ast.literal_eval(baza_gier) for baza_gier in baza_gier]

            print("Dane z pliku wczytano pomyślnie")
            print(baza_gier)

            print(menu)
        elif wybor == 12:
            break






