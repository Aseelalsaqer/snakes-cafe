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
print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")

print("**************************************")
for i in menu:
    print(i["type"])
    print("----------")
    for n in i["kind"]:
        print(n)
print("**************************************")
print("** What would you like to order? **")
print("**************************************")
