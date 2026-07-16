name = input("welcome to the cafe management!please enter your order: ")
print(f"hello, {name}! Welcome to the Cafe Management System?")
menu = {
    "coffee" : 20,
        "tea" : 15,
            "coffee" : 10,
                "burger" : 50,
                "juice" : 20,
                "sandwich" : 30,
                "pasta" : 40,
                "salad" : 25,
                "cake" : 300,
                "ice cream" : 60,
                "cookies" : 10,
}

print("here is our menu:")
for item, price in menu.items():
    print(f"{item}: {price} Rs")

order = []
while True:
    item = input("please enter the item you want to order (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    elif item in menu:
        order.append(item)
        print(f"{item} added to your order.")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")
        #order summary
        if order:
            print("\n---Your order summary:")
            total = 0
            for item, qty in order.item():
                subtotal = menu[item]* qty
                total += subtotal
                print(f"{item}: {price} Rs")
            print(f"Total: {total} Rs")

            if total>200:
                discount = total * 0.1
                total -= discount   
    print(f"Discount applied(10%) : Rs")
