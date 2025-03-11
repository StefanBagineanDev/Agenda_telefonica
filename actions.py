from os import system

# Constante

phones = []
names_surnames = []
LIMITA_MAXIMA = 100

#applicationFullPath = path.abspath(__file__)
#applicationPath = path.dirname(applicationFullPath) + "\\"

#PROGRAM_PATH = applicationPath

# Optiuni pentru meniu

OPTIUNE_ADAUGARE_CONTACT = '1'
OPTIUNE_CAUTARE_DUPA_NUME = '2'
OPTIUNE_STERGERE_CONTACT = '3'
OPTIUNE_AFISARE_CONTACTE = '4'
OPTIUNE_SCHIMBARE_LIMBA = '5'
OPTIUNE_EXIT = 'E'

limba = "ro"
SEPARATOR_MENIU = "-> "

# Functii utile

class Menu:
    def __init__(self):
        self.options = {
            "ro": ["Agenda telefonica", "Adaugare contact", "Cautare contact dupa nume", "Stergere contact", "Afisare contacte", "Schimbare limba", "Iesire din program"],
            "en": ["Phone Book", "Add contact", "Search contact by name", "Delete contact", "Show contacts", "Change language", "Exit program"],
            "fr": ["Annuaire téléphonique", "Ajouter un contact", "Rechercher un contact par nom", "Supprimer un contact", "Afficher les contacts", "Changer de langue", "Quitter le programme"]
        }
    def get_option(self, language, index):
        return self.options.get(language, self.options["ro"])[index]

menu = Menu()


def afisare_meniu():
    global limba
    print(' *****************')
    print(f"* {menu.get_option(limba, 0)} *")
    print(' *****************')
    print()
    print(OPTIUNE_ADAUGARE_CONTACT, SEPARATOR_MENIU, menu.get_option(limba, 1))
    print(OPTIUNE_CAUTARE_DUPA_NUME, SEPARATOR_MENIU, menu.get_option(limba, 2))
    print(OPTIUNE_STERGERE_CONTACT, SEPARATOR_MENIU, menu.get_option(limba, 3))
    print(OPTIUNE_AFISARE_CONTACTE, SEPARATOR_MENIU, menu.get_option(limba, 4))
    print(OPTIUNE_SCHIMBARE_LIMBA, SEPARATOR_MENIU, menu.get_option(limba, 5))
    print(OPTIUNE_EXIT, SEPARATOR_MENIU, menu.get_option(limba, 6))
    print()


def isLetter(caracter):
    return caracter.isalpha()


def validate_phone_number(phoneNumber):
    if not (2 < len(phoneNumber) <= 15):
        return False
    
    if phoneNumber[0] in "-." or phoneNumber.count("+") > 1 or "," in phoneNumber:
        return False
    
    return all(c.isdigit() or c == "+" for c in phoneNumber)


def menu_action_adaugare_contacte():
    if len(names_surnames) < LIMITA_MAXIMA:
        name_surname = input("Introduceti numele si prenumele: ")
        phone = input("Introduceti numarul de telefon: ")
        
        if validate_phone_number(phone):
            names_surnames.append(name_surname)
            phones.append(phone)
            print("Contactul a fost adaugat cu succes!\n")
        else:
            print("Numar de telefon invalid. Numarul trebuie sa contina numai numere intre 2 si 16 caractere\n")
    else:
        print("Agenda telefonica este plina. Nu mai puteti introduce contacte noi.")


def showEmptyPhoneBookMessage():
    print("Agenda nu contine contacte.")


def cautare_dupa_nume(contactName):
    contactNameLower = contactName.lower()
    for i, name in enumerate(names_surnames):
        if name.lower() == contactNameLower:
            return i
    return -1


def menu_action_cautare_dupa_nume():
    if not names_surnames:
        showEmptyPhoneBookMessage()
    else:
        numeCautat = input("Introduceti numele pe care il cautati: ")
        contactPoz = cautare_dupa_nume(numeCautat)
        if contactPoz > -1:
            print(f"{names_surnames[contactPoz]}: {phones[contactPoz]}")
        else:
            print("Numele cautat nu este in agenda.")


def menu_action_stergere_contact():
    if not names_surnames:      #if len(names_surnames) == 0:
        showEmptyPhoneBookMessage()
    else:
        numeDeSters = input("Introduceti numele contactului pe care doriti sa il stergeti: ")
        poz = cautare_dupa_nume(numeDeSters)
        if poz > -1:
            del names_surnames[poz]
            del phones[poz]
            print("Contactul a fost sters cu succes!")
        else:
            print("Numele cautat nu este in agenda.")


def menu_action_afisare_contacte():
    if not names_surnames:     #if len(names_surnames) == 0:
        showEmptyPhoneBookMessage()
    else:
        for i in range(len(names_surnames)):
            print(names_surnames[i], "-", phones[i])
        print()


def menu_action_schimbare_limba():
    global limba
    limbi_disponibile = ["ro", "en", "fr"]
    print("Limbi disponibile: ro, en, fr")
    noua_limba = input("Alegeti limba: ").strip().lower()
    if noua_limba in limbi_disponibile:
        limba = noua_limba
        print("\nLimba selectata cu succes.\n")
    else:
        print("\nLimba invalida. Incercati sa folositi: ro, en, fr.\n")


def main():
    optiune = ""

    while optiune != OPTIUNE_EXIT:
        afisare_meniu()
        optiune = input("Alegeti o optiune: ")
        print()
        if optiune == OPTIUNE_ADAUGARE_CONTACT:
            menu_action_adaugare_contacte()
        elif optiune == OPTIUNE_CAUTARE_DUPA_NUME:
            menu_action_cautare_dupa_nume()
        elif optiune == OPTIUNE_STERGERE_CONTACT:
            menu_action_stergere_contact()
        elif optiune == OPTIUNE_AFISARE_CONTACTE:
            menu_action_afisare_contacte()
        elif optiune == OPTIUNE_SCHIMBARE_LIMBA:
            menu_action_schimbare_limba()
        elif optiune == OPTIUNE_EXIT:
            print("Iesire din program.")
            break
        else:
            print("Optiune invalida. Reincercati!")

if __name__ == "__main__":
    main()

    #def menu_action_salvare():
 #   try:
  #      file = open(PROGRAM_PATH + "agendaTelefonica.csv", "w")
#
 #       if len(names_surnames) == 0:
  #          showEmptyPhoneBookMessage()
   #     else:
    #        for i in range(len(names_surnames)):
     #           file.write(names_surnames[i] + "," + phones[i])
      #          file.write("\n")
       #     print("Agenda a fost salvata cu succes! ")
        #file.close()
    #except FileNotFoundError:
     #   print("Prima folosire a aplicatiei. Trebuie sa adaugati contacte si sa le salvati. ")


#def menu_action_load():
 #   global names_surnames, phones
#
 #   try:
  #      file = open(PROGRAM_PATH + "agendaTelefonica.csv", "r")
#
 #       for row in file:
  #          poz = row.find(",")

   #         if poz > -1:
    #            key = row[0 : poz]
     #           value = row[poz + 1 :]

#                names_surnames.append(key)
 #               phones.append(value)

  #          else:
   #             print("Agenda nu contine contacte. ")
    #    file.close()
     #   print("Agenda a fost incarcata cu succes! ")
    #except FileNotFoundError:
     #   print("Prima folosire a aplicatiei. Trebuie sa adaugati contacte si sa le salvati. ")
