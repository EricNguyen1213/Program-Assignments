# Step 1
empty_list = []

# Step 2
US_cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(US_cities)

# Step 3
random_word_list = ["duck", "eye", "Vic", "sucks", "banana", "university", "work", "snickers", "yummy", "yoyo"]
print(random_word_list)

three_cities = US_cities[0:3]
print(three_cities)
print(random_word_list[0])
print(random_word_list[4])
print(random_word_list[9])

# Step 4
four_random_words = random_word_list[6:10]
print(four_random_words)

# Step 5
US_cities[0] = "San Francisco"
US_cities[2] = "Brooklyn"
US_cities[7] = "Hollywood"
US_cities[5] = "Tampa"
print(US_cities)

US_cities.append("New Jersey")
US_cities.extend(["Santa Cruz", "Selma", "Chicago"])
US_cities.insert(7, "Washington, D.C.")
print(US_cities)

# Step 6
US_cities.append("Oakland")
US_cities.extend(["New York City", "Los Angeles"])
US_cities.insert(0, "Miami")
print(US_cities)

# Step 7
del US_cities[5]
US_cities.pop(14)
US_cities.remove("Brooklyn")
print(US_cities)

# Lab 4 Step 8-9
def nameEveryCity():
    for city in US_cities:
        print(city)

def nameEveryCityAgain():
    i = 0
    while i < len(US_cities):
        print(US_cities[0])
        i += 1

def nameLongerCity():
    for i in range(len(US_cities)-1):
        if len(US_cities[i]) > len(US_cities[i-1]):
            print(US_cities[i])
nameLongerCity()

# Step 10
