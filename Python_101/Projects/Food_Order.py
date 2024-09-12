MENU = {
    "Lugaw Plain",
    "Lugaw Plain w/ egg",
    "Goto",
    "Goto w/ egg",
    "Goto Overload",
    "Beef Mami",
    "Beef Mami w/ egg",
    "Tokwa't Baboy",
    "Tokwa",
    "Egg",
    "Lumpia Togue",
    "Extra Laman",
    "Mami Pares",
    "Beef Pares",
    "Beef Pares w/ rice",
    "Lechon Pares",
    "Lechon Pares w/ rice",
    "Plain rice",
}


DRINKS = {
    "Mountain Dew",
    "Coke",
    "Royal",
    "RC Cola",
    "Lemon",
    "Mineral Water (Small)",
    "Mineral Water (Big)",
}


def get_order():
    current_order = []
    while True:
        item = input("Enter an item from the menu (or 'done' to finish): ")
        if item.lower() == "done":
            break
        elif item.title() in MENU:
            current_order.append(item.title())
        else:
            print(f"{item} is not a valid item. Please try again.")
