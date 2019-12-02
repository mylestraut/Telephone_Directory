main_dict = {}

def print_phonebook():
    for m in main_dict.keys():
        print(main_dict[m][0] + " " + main_dict[m][1] + ":\t" + main_dict[m][2])

def write_file():
    outfile = open("numbers.txt", "w")
    for k in main_dict.keys():
        outfile.write(k + ":" + main_dict[k][2] + "\n")
    outfile.close()

def read_file():
    
    infile = open("numbers.txt", "r")
    for inline in infile:
        inline = inline.rstrip("\n")
        name, number = inline.split(":")
        firstname, surname = name.split(" ")

        main_dict[name] = []
        main_dict[name].append(firstname)
        main_dict[name].append(surname)
        main_dict[name].append(number)

    infile.close()

    
def add_num(Name, Surname, Number):

    read_file()
    for z in main_dict.values():
        contact = z

    if Name and Surname in contact:
        print("Contact already exists.")

    else:
        outfile = open("numbers.txt", "a")
        outfile.write(Name + " " + Surname + ":" + Number + "\n")
        outfile.close

def print_menu():
    print("PHONEBOOK")
    print("1:\tAdd Name and Number")
    print("2:\tPrint Phonebook")
    print("3:\tEdit Phonebook")
    print("4:\tSearch")
    print("5:\tDelete Number")
    print("6:\tQuit")
    print()

def search_menu():
    print("1:\tSearch By Name")
    print("2:\tSearch By Surname")
    print("3:\tReturn")

def del_num(First_name, Last_name):
    read_file()

    full_name = str(First_name + " " + Last_name)
    if full_name in main_dict.keys():
        del main_dict[full_name]
        print(full_name + " was sucessfully deleted.")

    write_file()

def edit_menu():
    print("1:\tEdit Firstname")
    print("2:\tEdit Surname")
    print("3:\tEdit Number")
    print("4:\tReturn")
    
def edit_contact(edit):
    read_file()
    
    if edit in main_dict.keys():
        edit_menu()
        print()
        edit_choice = int(input("Please make a choice:\t"))

        if edit_choice == 1:
            new_firstname = input("Enter New Name:\t")
            main_dict[edit][0] = new_firstname
            new_key = main_dict[edit][0] + " " + main_dict[edit][1]
            main_dict[new_key] =  main_dict.pop(edit)
            

        elif edit_choice == 2:
            new_surname = input("Enter New Surname:\t")
            main_dict[edit][1] = new_surname
            new_key = main_dict[edit][0] + " " + main_dict[edit][1]
            main_dict[new_key] =  main_dict.pop(edit)
            

        elif edit_choice == 3:
            new_number = input("Enter New Number:\t")
            main_dict[edit][2] = new_number
            

        elif edit_choice == 4:
            print()
            
    else:
        print("Name not found.")
        print()
        
    

print_menu()    

while True:
    menu_choice = int(input("Please make a choice:\t"))

    if menu_choice == 1:
        Name = input("\nEnter Name: ")
        Surname = input("Enter Surname: ")
        Number = input("Enter Number: ")
        add_num(Name, Surname, Number)
        print()
        print_menu()

    elif menu_choice == 2:
        read_file()
        print()
        print_phonebook()
        print()
        print_menu()

    elif menu_choice == 3:
        read_file()
        print()
        edit = input("Please enter contact to edit: ")
        edit_contact(edit)
        write_file()
        print()
        print_menu()
        
    elif menu_choice == 4:
        read_file()
        search_menu()
        print()
        Search_choice = int(input("Please make a choice:\t"))
        
        if Search_choice == 1:
            NAME = input("\nPlease Enter Name To Search: ")
            print()
            for h in main_dict.values():
                if NAME in h:
                    print(full[0] + " " + full[1] + ":\t" + full[2])

        elif Search_choice == 2:
            SURNAME = input("\nPlease Enter Surname To Search: ")
            print()
            for o in main_dict.values():
                if SURNAME in o:
                    print(o[0] + " " + o[1] + ":\t" + o[2])

        elif Search_choice == 3:
            print()

        print()
        print_menu()

    elif menu_choice == 5:
        print()
        First_name = input("Enter First Name:\t")
        Last_name = input("Enter Last Name:\t")
        del_num(First_name, Last_name)
        print()
        print_menu()
        
    elif menu_choice == 6:
        print("Goodbye")
        break


