def main():

    keep_going = "y"
    while keep_going == "y":
        print("Heroes Program\n", sep=" ", end="")
        func_heroes = int(input("Choose your function Heroes Program \n"
                                "1. Display Heroes\n"
                                "2. Add Heroes\n"
                                "3. Insert Heroes\n"
                                "4. Remove Heroes\n"
                                "5. Display Sorted Heroes (Ascending/Descending)\n"
                                "Enter choice (1-5): "))
        if func_heroes == 1:
            Display_Heroes()
        elif func_heroes == 2:
            Add_Heroes()
        elif func_heroes == 3:
            Insert_Heroes()
        elif func_heroes == 4:
            Remove_Heroes()
        elif func_heroes == 5:
            Display_Sorted_Heroes()
        else:
            return print("End Program")


def Display_Heroes():
    print(HEROES)

def Add_Heroes():
    new_hero = input("Enter add Hero name: ")
    HEROES.append(new_hero)
    return HEROES

def Insert_Heroes():
    index_hero = int(input("Enter index in HEROES: "))
    ins_hero = input("Enter Hero name: ")
    HEROES.insert(index_hero, ins_hero)
    return HEROES

def Remove_Heroes():
    rem_hero = input("Enter Hero name to remove: ")
    HEROES.remove(rem_hero)
    return HEROES

def Display_Sorted_Heroes():
    choice_sorted = int(input("Enter choice to sorted Hero (1-2): "))
    if choice_sorted == 1:
        HEROES.sort()
    elif choice_sorted == 2:
        HEROES.reverse()
    else:
        print("Error")
    return HEROES

HEROES = ['Ironman', 'Thor', 'Hulk', 'Spiderman']

main()