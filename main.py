menu = {
    "pizza" : 49,
    "pasta" : 80,
    "burger" : 60,
    "shanwitch": 40,
    "coffe": 50
}
print("welcome to python resturent menu")
print("pizza: RS.40\npasta: RS.40\nburger RS.60\nshanwitch RS.40\ncoffe RS.50")

order_total = 0

item_1 = input("enter the name of iteam you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your iteam {item_1} has been added to your order")
else:
    print(f"plese order something else ew can surve")

another_order = input("do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("entern the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"iteam {item_2} has been added to order")
else:
    print(f"thank you for your order")
    
print(f"the total amount of iteam to pay is {order_total}")




