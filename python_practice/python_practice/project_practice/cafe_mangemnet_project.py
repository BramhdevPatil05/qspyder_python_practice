menu={'Pasta':45,'Pizza':60,'Burger':70,'Salad':80,'Coffee':80}

print('Welcome to Python Cafe')
print('Pasta:45\nPizza:60\nBurger:70\nSalad:80\nCoffee:80')

Order_Total=0

Item1=input('Add an item u like:')
if Item1 in menu:
    Order_Total += menu[Item1]
    print(f"Item is selected")
else:
    print(f'Item not available at the moment\nChoose another Item')

Another_Order=input('Do u want to add another Item from the Menu(Yes/No)')

if Another_Order=='Yes':
    Item2=input('Add an item from the Menu')
    if Item2 in menu:
        Order_Total += menu[Item2]
        print(f"Item is selected")
    else:
        print(f'Item not available at the moment\nChoose another Item')

print(f'Total amount of items is {Order_Total}')