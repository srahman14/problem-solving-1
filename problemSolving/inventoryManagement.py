import time

# This is the Inventory, defined as a dictionary
# Each key is an item in the store, and the key holds two values
# One for quantity and the other for price, in this order respectively
dict_inv = {"dresses": [100, 35], "footwear": [50, 75], "tops": [
    120, 45], "jewelry": [12, 400], "bags": [30, 40]}


print("Welcome to your inventory! \n Inventory options: ")
while True:
    time.sleep(1)
    print("\n 1. Add Inventory \n 2. Update Inventory \n 3. Remove items from Inventory \n 4. Display Inventory \n 5. Calculate Total Inventory \n 6. Exit")
    # This is used to track the selection that the user would like, after each iteration it is set back to 0
    # This ensures the next while loop will work properly
    option = 0

    while option < 1 or option > 6:
        option = int(input("Enter option 1-5: "))
    # OPTION 1: Add to Inventory
    if option == 1:
        selection = input("Enter the item name to add to inventory: ")

        # .strip() removes the whitespace, i.e. an empty string will not be valid
        while selection.strip() == "":
            selection = input("Enter the item name to add to inventory: ")
            if selection.strip() != "":
                break

        selection_quantity = 0
        while True:
            # While the selection_quantity is not equal to an interger, the user is thrown an error
            try:
                selection_quantity = int(
                    input(f"Enter the quantity of {selection}: "))
                break
            except ValueError:
                print(
                    f"'{selection_quantity}' is an invalid input, this should be an interger")

        selection_price = 0
        while True:
            # While the selection_price is not equal to an float, the user is thrown an error
            try:
                selection_price = float(
                    input(f"Enter the price of {selection}: "))
                break
            except ValueError:
                print(
                    f"'{selection_price}' is an invalid input, this should be an interger")
        # Value holds both the quantity and price
        value = [selection_quantity, selection_price]
        # Update the dictionary with a new input -> here it is the value
        dict_inv[f"{selection}"] = value
    # OPTION 2: Update Inventory
    elif option == 2:
        update_item = input("Enter the item you wish to update: ")
        # This will be the new updated value the user wants to enter
        update_new = ""
        # While the item does not exist in the dictionary
        while update_item not in dict_inv:
            print("Item is not in the inventory, try again")
            update_item = input("Enter the item you wish to update: ")

        # User given option to update quantity or price
        update_type = input(
            "Enter the type you wish to update: Quantity (Q) / Price (P) ")

        if update_type.lower == "q":
            # While the desired updated value is empty
            while update_new == "":
                update_new = int(input("Enter the new quantity: "))
                # Break case when intereger corectly inputted
                if update_new != "":
                    dict_inv[f"{update_item}"][0] = update_new
                    break
        else:
            while update_new == "":
                update_new = float(input("Enter the new price: "))
                # Break case when float corectly inputted
                if update_new != "":
                    dict_inv[f"{update_item}"][1] = update_new
                    break
    # OPTION 3: Remove from Inventory
    elif option == 3:
        print(dict_inv)
        # This is used to enable the while loop
        remove_item = None
        # While the item the user wants to remove is not existing in the inventory
        while remove_item not in dict_inv:
            remove_item = input("Enter the item you wish to remove: ")
            # If the value the user has entered does not exist, throw an error and skip the rest
            # of the code back to the next iteration
            if remove_item not in dict_inv:
                print(f"{remove_item} does not exist in the inventory try again. \n")
                continue
            else:
                print(f"{remove_item} has successfully been removed!")
        # Using the .pop() function, the value is removed
        dict_inv.pop(f"{remove_item}")
        print("\nUpdated Inventory:", "\n", dict_inv)

    # OPTION 4: Display Inventory
    elif option == 4:
        print("Item    Quantity  Price")
        # Every key is iterated through to return the name, quantity and price
        for key in dict_inv:
            # Key is the item name
            # Using the key to access the elements it is equal to
            # Here index of 0 refers to quantity and 1 refers to price
            print(key + "  ", dict_inv[f"{key}"][0],
                  "   ", dict_inv[f"{key}"][1],  "\n")
    # OPTION 5: Calculate Inventory
    elif option == 5:
        total = 0
        # Using the same logic above, iterate through every key
        for key in dict_inv:
            # Multiply the quantity with the price for every item and
            # add it to the total
            total += dict_inv[f"{key}"][0] * dict_inv[f"{key}"][1]

        print("Calculating...")
        time.sleep(1)
        print(f"£{total}, is the total inventory value")
    # OPTION 6: Exit Inventory
    elif option == 6:
        # Additional option to exit the inventory and stop the while loop
        print("Exiting...")
        time.sleep(1)
        print("EXITED")
        break
