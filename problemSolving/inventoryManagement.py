import time

# This is the Inventory, defined as a dictionary
# Each key is an item in the store, and the key holds two values
# One for quantity and the other for price, in this order respectively
inventory_dict = {"dresses": [100, 35], "footwear": [50, 75],
                  "tops": [120, 45], "jewelry": [12, 400], "bags": [30, 40],
                  "cards": [10, 12], "jeans": [45, 99]
                  }


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
        # furthermore, an item that already exists cannot be added again
        # I remove the whitespace from an input that already exists too as an input with the
        # same name but additional space will be counted as a different item
        while selection.strip() == "" or selection.strip() in inventory_dict:
            if selection.strip() == "":
                selection = input(
                    "You cannot enter an empty input \nEnter the item name again to add to inventory: ")
            elif selection.strip() in inventory_dict:
                selection = input(
                    f"{selection.strip().capitalize()} already exists in inventory! \nEnter the item name again to add to inventory: ")
            else:
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
        inventory_dict[f"{selection}"] = value

    # OPTION 2: Update Inventory
    elif option == 2:
        update_item = input("Enter the item you wish to update: ")
        # This will be the new updated value the user wants to enter
        update_new = ""
        # While the item does not exist in the dictionary
        while update_item.strip().lower not in inventory_dict:
            print(
                f"{update_item.strip().capitalize()} is not in the inventory, try again")
            update_item = input("Enter the item you wish to update: ")

        # User given option to update quantity or price
        update_type = input(
            "Enter the type you wish to update: Quantity (Q) / Price (P) ")

        # If the update type is for quantity
        if update_type.strip().lower == "q":
            # While the desired updated value is empty
            while update_new == "":
                update_new = int(input("Enter the new quantity: "))
                # Break case when intereger corectly inputted
                if update_new != "":
                    inventory_dict[f"{update_item.strip().lower}"][0] = update_new
                    break
        # Else if the update tyoe is for price
        else:
            while update_new == "":
                update_new = float(input("Enter the new price: "))
                # Break case when float corectly inputted
                if update_new != "":
                    inventory_dict[f"{update_item.strip().lower}"][1] = update_new
                    break
    # OPTION 3: Remove from Inventory
    elif option == 3:
        print(inventory_dict)
        # This is used to enable the while loop
        remove_item = None
        # While the item the user wants to remove is not existing in the inventory
        while remove_item.strip().lower not in inventory_dict:
            remove_item = input("Enter the item you wish to remove: ")
            # If the value the user has entered does not exist, throw an error and skip the rest
            # of the code back to the next iteration
            if remove_item.strip().lower not in inventory_dict:
                print(f"{remove_item} does not exist in the inventory try again. \n")
                continue
            else:
                print(f"{remove_item} has successfully been removed!")
        # Using the .pop() function, the value is removed
        inventory_dict.pop(f"{remove_item}")
        print("\nUpdated Inventory:", "\n", inventory_dict)

    # OPTION 4: Display Inventory
    elif option == 4:
        print("Item    Quantity   Price")
        # Every key is iterated through to return the name, quantity and price
        for key in inventory_dict:
            # Key is the item name
            # Using the key to access the elements it is equal to
            # Here index of 0 refers to quantity and 1 refers to price
            print(key + "  ", inventory_dict[f"{key}"][0],
                  "   ", inventory_dict[f"{key}"][1],  "\n")
    # OPTION 5: Calculate Inventory
    elif option == 5:
        total = 0
        # Using the same logic above, iterate through every key
        for key in inventory_dict:
            # Multiply the quantity with the price for every item and
            # add it to the total
            total += inventory_dict[f"{key}"][0] * inventory_dict[f"{key}"][1]

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
