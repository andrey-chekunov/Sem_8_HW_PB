def print_data(data):
    if len(data) > 0:
        print("Second Name".center(20), "First Name".center(20), "Phone Number".center(20), "Note".center(30))
        print("-"*85)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(30))
    else:
        print("Phonebook is EMPTY!")