dict_inv = {"dresses": [200, 35], "footwear": [300, 75]}


# # add_inventory(dict_inv)
# # print(dict_inv)
# # add_inventory(dict_inv)
# # print(dict_inv)
# # update_inventory(dict_inv)
# # print(dict_inv)

# def remove_inventory(inventory):
#     print(inventory)
#     remove_item = None
#     while remove_item not in inventory:
#         remove_item = input("Enter the item you wish to remove: ")
#         if remove_item not in inventory:
#             print(f"{remove_item} does not exist in the inventory try again. \n")
#         else:
#             print(f"{remove_item} has successfully been removed!")
#             continue

#     inventory.pop(f"{remove_item}")
#     print("\nUpdated Inventory:", "\n", inventory)


# def display_inventory(inventory):
#     print("Item Quantity Price")
#     for key in inventory:
#         # Cannot concatenate list with string, so use commas
#         # Need to work on formatting the position of the numbers
#         print(key + "  ", inventory[f"{key}"][0],
#               "  ", inventory[f"{key}"][1],  "\n")


# def calculate_inventory(inventory):
#     total = 0
#     for key in inventory:
#         total += inventory[f"{key}"][0] * inventory[f"{key}"][1]

#     print(f"£{total}, is the total inventory value")

print("Welcome to your inventory! \n Inventory options: ")
while True:
    print(" 1. Add Inventory \n 2. Update Inventory \n 3. Remove items from Inventory \n 4. Display Inventory \n 5. Calculate Total Inventory")
    option = 0

    while option < 1 or option > 5:
        option = int(input("Enter option 1-5: "))

    if option == 1:
        selection = input("Enter the item name to add to inventory: ")

        while selection.strip() == "":
            selection = input("Enter the item name to add to inventory: ")
            if selection.strip() != "":
                break

        selection_quantity = 0
        while True:
            try:
                selection_quantity = int(
                    input(f"Enter the quantity of {selection}: "))
                break
            except ValueError:
                print(
                    f"'{selection_quantity}' is an invalid input, this should be an interger")

        selection_price = 0
        while True:
            try:
                selection_price = float(
                    input(f"Enter the price of {selection}: "))
                break
            except ValueError:
                print(
                    f"'{selection_price}' is an invalid input, this should be an interger")

        value = [selection_quantity, selection_price]
        dict_inv[f"{selection}"] = value

    elif option == 2:
        update_item = input("Enter the item you wish to update: ")

        while update_item not in dict_inv:
            print("Item is not in the inventory, try again")
            update_item = input("Enter the item you wish to update: ")

        update_type = input(
            "Enter the type you wish to update: Quantity (Q) / Price (P) ")
        update_new = ""

        if update_type.lower == "q":
            update_new = ""
            while update_new == "":
                update_new = int(input("Enter the new quantity: "))
                if update_new != "":
                    dict_inv[f"{update_item}"][0] = update_new
                    break
        else:
            while update_new == "":
                update_new = float(input("Enter the new price: "))
                if update_new != "":
                    dict_inv[f"{update_item}"][1] = update_new
                    break
