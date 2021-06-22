# Step 1 & 2
product_costs = {"chicken":1.59,"beef":1.99,"cheese":1.00,"milk":2.50}

# Step 3
my_favorite = {"subject": "CS","color": "purple", "number": 7, "hobby": "sleeping"}

# Step 4
chicken = product_costs["chicken"]
print(chicken)
beef = product_costs["beef"]
print(beef)
cheese = product_costs["cheese"]
print(cheese)
milk = product_costs["milk"]
print(milk)

subject = my_favorite["subject"]
print(subject)
color = my_favorite["color"]
print(color)
number = my_favorite["number"]
print(number)
hobby = my_favorite["hobby"]
print(hobby)

# Step 5
my_favorite["number"] -= 14

# Step 6
shoe_inventory = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk":20}

# Step 7
shoe_inventory["SB Dunk"] -= 2
shoe_inventory["Yeezy"] += 1
shoe_inventory["Jordan 13"] += 7
shoe_inventory["Yeezy"] += 7
shoe_inventory["Foamposite"] += 7
shoe_inventory["Air Max"] += 7
shoe_inventory["SB Dunk"] += 7
shoe_inventory["Jordan 13"] -= 3
shoe_inventory["Yeezy"] -= 3
shoe_inventory["Foamposite"] -= 3
shoe_inventory["Air Max"] -= 3
shoe_inventory["SB Dunk"] -= 3

# Step 8
product_costs = {"chicken":1.59, "beef":1.99, "cheese":1.00, "milk":2.50, "pork":2.75, "egg":0.75, "fish":3.00}
my_favorite = {"subject":"CS", "color":"purple", "number":7, "hobby":"sleeping", "book":"Story Thieves", "movie":"A Silent Voice", "food":"sushi"}
shoe_inventory = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk":20, "Under Armour": 7, "Nike": 12, "Sketchers": 22}

# Step 9
del product_costs["fish"]
del product_costs["pork"]
print(product_costs)

del my_favorite["book"]
del my_favorite["subject"]
print(my_favorite)

del shoe_inventory["Foamposite"]
del shoe_inventory["Nike"]
print(shoe_inventory)

# Function Practice
# Step 2
def total_price(*argv):
    grocery_list = []
    total_sum = 0
    written_grocery_list = ""
    for arg in argv:
        if arg in product_costs:
            grocery_list.append(arg)
            total_sum += product_costs[arg]
    for item in grocery_list:
        if item == grocery_list[-1]:
            written_grocery_list += " and " + item
        elif len(grocery_list) == 2:
            written_grocery_list += " " + item
        else:
            written_grocery_list += " " + item + ","
    final_statement = "The total price of" + written_grocery_list + " is " + str(total_sum)
    return final_statement
#print(total_price("beef", "cheese", "water", "chicken"))

# Step 3
def price_difference(food1, food2):
    total_difference = 0
    if food1 in product_costs and food2 in product_costs:
        if product_costs[food1] > product_costs[food2]:
            total_difference = product_costs[food1] - product_costs[food2]
        else:
            total_difference = product_costs[food2] - product_costs[food1]
        return("The difference between " + food1 + " and " + food2 + " is " + str(total_difference))
    else:
        return("The difference between " + food1 + " and " + food2 + " is 0 because one of the items are not in store.")
#price_difference("beef", "cheese")

def price_sum_and_difference(*argv):
    print(total_price(*argv))
    print(price_difference(argv[0],argv[1]))
price_sum_and_difference("beef", "cheese")

# Step 4
def restock(selected, multiplier):
    if selected in shoe_inventory:
        shoe_inventory[selected] *= multiplier
    elif selected == "all":
        for key in  shoe_inventory:
            shoe_inventory[key] *= multiplier
    return shoe_inventory
print(restock("all", 2))

# Step 5

def clearance_sale(selected, divisor):
    if selected in shoe_inventory:
        shoe_inventory[selected] /= divisor
    elif selected == "all":
        for key in  shoe_inventory:
            shoe_inventory[key] /= divisor
    return shoe_inventory

def restock_or_clearance(operation, selected, scale):
    if operation == "multiply" or operation == "*":
        restock(selected, scale)
    else if operation == "divide" or operation == "/":
        clearance_sale(selected, scale)

print(restock_or_clearance("*", "Yeezy", 3))

# Step 6
def operate_on_my_favs_to_gen_nums(operator, selected1, selected2):
    result = 0
    if operator == "%" and operator == "module":
        result = len(my_favorite[selected1]) % len(my_favorite[selected2])
        return result
    elif operator == "//" and operator == "floor division":
        result = len(my_favorite[selected1]) // len(my_favorite[selected2])
        return result
    elif operator == "**" and operator == "exponential":
        result = len(my_favorite[selected1]) // len(my_favorite[selected2])
        return result
