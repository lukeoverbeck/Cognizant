# Task 1
fruit = ["blueberries", "pineapples", "bananas", "strawberries", "raspberries"]
print(f"Original list: {fruit}")

fruit.append("mangoes")
print(f"After adding a fruit: {fruit}")

fruit.remove("strawberries")
print(f"After removing a fruit: {fruit}")

print(f"Reversed list: {fruit[::-1]}")

print()

# Task 2
self = {"name": "Luke Overbeck", "age": 21, "city": "Haddonfield"}
self.update({"favorite color": "blue"})
self["city"] = "Philadelphia"

# To get the output in the example, I had to add the elements to a list and then
# join the list
keys_list = []
for key in self.keys():
 keys_list.append(key)
print("Keys:", ", ".join(keys_list))

values_list = []
for value in self.values():
 values_list.append(str(value))
print("Values:", ", ".join(values_list))

print()

# Task 3
my_tuple = ("Mulan", "I Am The Highway", "Harry Potter and the Goblet of Fire")
print(f"Favorite things: {my_tuple}")

# Using a try/except block was necessary to get the output in the example
try:
 my_tuple.add("Orange juice")
except:
 print("Oops! Tuples cannot be changed.")

print(f"Length of tuple: {len(my_tuple)}")
