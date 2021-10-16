

menu = [
    {
        "name": "Appetizers",
        "available_types": ["Wings", "Cookies", "Spring Rolls"]
    }, {
        "name": "Entrees",
        "available_types": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
    }, {
        "name": "Desserts",
        "available_types": ["Ice Cream", "Cake", "Pie"]
    }, {
        "name": "Drinks",
        "available_types": ["Coffee", "Tea", "Unicorn Tears"]
    }
]
available_menu = ['wings', 'cookies',
                  'spring rolls', 'salmon',
                  'steak', 'meat tornado',
                  'a literal garden', 'ice Cream',
                  'cake', 'pie', 'coffee',
                  'tea', 'unicorn tears']


def handle_print():
    """this function will prent the welcoming msg to the user
    takes no argument
    return nothing"""
    print("""**************************************
**    Welcome to the Snakes Cafe!:snake: **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")
    for i in menu:
        print(i["name"])
        print("----------")
        for y in i["available_types"]:
            print(y)
    print()
    print("""***********************************
** What would you like to order? **
***********************************""")


order_list = []


def handle_order():
    """this function will take the user order and will add it to a list and will keep asking the user for the next item until the user type quit also will count how many time the user asked for the same order also if the user type an order not in the list the function will till him to type from the menu and will provide the user of how many time asked for the same order """
    order = input("> ")
    if order != "quit":
        if order in available_menu:
            order_list.append(order)
            if order in order_list:
                count = 0
                for i in order_list:
                    if i == order:
                        count += 1
                print(
                    f"** {count} order of {order} have been added to your meal **")
                handle_order()
            else:
                order_list.append(order)
                print(f"** 1 order of {order} have been added to your meal **")
                handle_order()
        else:
            print(f"please choose item form the menu or type quit to quit")
            handle_order()
    else:
        return


if __name__ == "__main__":
    handle_print()
    handle_order()


# menu = [
#     {
#         "type": "Appetizers",
#         "kind": ["Wings", "Cookies", "Spring Rolls"]
#     }, {
#         "type": "Entrees",
#         "kind": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
#     }, {
#         "type": "Desserts",
#         "kind": ["Ice Cream", "Cake", "Pie"]
#     }, {
#         "type": "Drinks",
#         "kind": ["Coffee", "Tea", "Unicorn Tears"]
#     },
# ]

# avalibale = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado",
#              "A Literal Garden""Ice Cream", "Cake", "Pie""Coffee", "Tea", "Unicorn Tears"]
# print("**************")
# print("*    Welcome to the Snakes Cafe!   *")
# print("*    Please see our menu below.    *")
# print("**")
# print('* To quit at any time, type "quit" *')
# for i in menu:
#     print(i["type"])
#     print("----------")
#     for y in i["kind"]:
#         print(y)
#         print()
# print("**************")

# orders = []
# if __name__ == "__main__":
#     order_counter = 1

#     x = ''
#     x2 = ''
#     while x != "quit":
#         x = input(f"* What would you like to order? *>")
#         if x not in avalibale:
#             print("your order does not exist please try again")
#         elif x in avalibale:
#             if x in orders:

#                 order_counter += 1
#                 print("**************")

#                 print(
#                     f"* {order_counter} orders of {x} have been added to your meal *")
#             elif x not in orders:
#                 order_counter2 = 0
#                 x2 = x
#                 orders.append(x2)
#                 order_counter2 += 1
#                 print("**************")
#                 print(
#                     f"* {order_counter2} order of {x2} have been added to your meal *")
#     print("This is The List of your oreder..")
#     for i in range(len(orders)):
#         print(orders[i], sep="\n")

    # order_counter = 0
    # orders = []
    # x = ''
    # while x != "quit":
    #     x = input(f"* What would you like to order? *>")
    #     if x != 'quit':
    #         orders.append(x)
    #         order_counter += 1
    #     elif x == 'quit':
    #         print("**************")
    #     print(
    #         f"* {order_counter} order of {x} have been added to your meal *")
    #     print("This is The List of your oreder..")
    #     for i in range(len(orders)):
    #         print(orders[i], sep="\n")
    # print("**************")
