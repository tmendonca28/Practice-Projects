# make a list to hold the items
shopping_list = []

# print out instructions on how to use the app
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")
print("Enter 'HELP' to view helpful commands")


while True:
    # ask for new items
    new_item = input("> ")
    # quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'SHOW':
        for idx, item in enumerate(shopping_list, start=1):
            print(idx, ". " + item)
        choice = input("Continue adding items? (Y/N) > ")
        if choice == "Y":
            continue
        else:
            break
    elif new_item == "HELP":
        print("Type 'SHOW' to view the current list and 'DONE' to finish writing your list")
        continue
    # add new items to the list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items".format(new_item, len(shopping_list)))


# print out the list
print("Here's your list: ")
for idx, item in enumerate(shopping_list, start=1):
    print(idx, ". " + item)
