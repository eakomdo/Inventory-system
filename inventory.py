#Build a basic inventory system for a small shop using Python. It will allow users to:

# View all items

# Add a new item

# Update item stock

# Delete an item

#  ** Calculate total stock value



Inventory = {
    "items_1": {
        "name": "Google Pixel 10",
        "quantity": 10,
        "price": 5.0
    },

    "items_2": {
        "name": "Candy",
        "quantity": 20,
        "price": 3.0
    },

    "items_3": {
        "name": "Macbook Pro 2024",
        "quantity": 15,
        "price": 7.5
    },

    "items_4": {
        "name": "Rolls Royce",
        "quantity": 5,
        "price": 10.0
    },

    "items_5": {
        "name": "iPhone 15",
        "quantity": 8,
        "price": 6.0
    }
}


#View all items
print("Current Inventory:")
print("-" * 30)

print(f"Item 1: {Inventory['items_1']['name']}")
print(f"Quantity: {Inventory['items_1']['quantity']}, Price: ${Inventory['items_1']['price']}")

print(f"Item 2: {Inventory['items_2']['name']}")
print(f"Quantity: {Inventory['items_2']['quantity']}, Price: ${Inventory['items_2']['price']}")

print(f"Item 3: {Inventory['items_3']['name']}")
print(f"Quantity: {Inventory['items_3']['quantity']}, Price: ${Inventory['items_3']['price']}")

print(f"Item 4: {Inventory['items_4']['name']}")
print(f"Quantity: {Inventory['items_4']['quantity']}, Price: ${Inventory['items_4']['price']}")

print(f"Item 5: {Inventory['items_5']['name']}")
print(f"Quantity: {Inventory['items_5']['quantity']}, Price: ${Inventory['items_5']['price']}")


# Add a new item