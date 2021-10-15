menu = [
    {
        "type": "Appetizers",
        "kind": ["Wings", "Cookies", "Spring Rolls"]
    }, {
        "type": "Entrees",
        "kind": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
    }, {
        "type": "Desserts",
        "kind": ["Ice Cream", "Cake", "Pie"]
    }, {
        "type": "Drinks",
        "kind": ["Coffee", "Tea", "Unicorn Tears"]
    },
]
print("**************")
print("*    Welcome to the Snakes Cafe!   *")
print("*    Please see our menu below.    *")
print("**")
print('* To quit at any time, type "quit" *')
for i in menu:
    print(i["type"])
    print("----------")
    for y in i["kind"]:
        print(y)
        print()
print("**************")


if __name__ == "__main__":
    order_counter = 0
    orders = []
    x = ''
    while x != "quit":
        x = input(f"* What would you like to order? *>")
        if x != 'quit':
            orders.append(x)
            order_counter += 1
        elif x == 'quit':
            print("**************")
        print(
            f"* {order_counter} order of {x} have been added to your meal *")
        print("This is The List of your oreder..")
        for i in range(len(orders)):
            print(orders[i], sep="\n")
            # print("**************")
