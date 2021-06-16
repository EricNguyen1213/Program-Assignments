product_costs = {"chicken":"$1.59","beef":"$1.99","cheese":"$1.00","milk":"$2.50"}
my_favorite = {"subject": "CS","color": "purple", "number": 7, "hobby": "sleeping"}


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

my_favorite["number"] -= 14

shoe_inventory = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk":20}

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
