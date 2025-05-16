inventory = {}

def addItem():
  key = input("Enter an item: ")

  quantity = int(input("Enter the quantity: "))
  price = float(input("Enter the price: "))

  value_tuple = (quantity, price)

  inventory.update({key: value_tuple})
  print("Added item.")

def removeItem():
  key = input("Enter an item to be removed: ")
  if key in inventory:
    del inventory[key]
    print("Item removed successfully.")
  else:
    print("Item not found.")

def updateQuantity():
  key = input("Enter an item to change its value: ")

  if key in inventory:
    quantity = int(input("Enter a new quantity: "))
    price = float(input("Enter a new price: "))
    new_tuple = (quantity, price)

    inventory[key] = new_tuple
    print("Item value changed successfully.")
  else:
    print("Item not found.")

x = 1
while x == 1:
  num = int(input("Main menu:\n" \
  "1. Add a new item to the inventory\n" \
  "2. Remove an item from the inventory\n" \
  "3. Update the quantity or price of an existing item\n" \
  "4. Exit\n"))

  if num == 1:
    addItem()
  elif num == 2:
    removeItem()
  elif num == 3:
    updateQuantity()
  elif num == 4:
    break
  else:
    print("Invalid option. Try again.")

print("\nFinal inventory: ")
total = 0
for key, value in inventory.items():
  print(f"Item: {key}, Quantity: {value[0]}, Price: ${value[1]}")
  total += value[0] * value[1]
print(f"Total value of inventory: {total}")