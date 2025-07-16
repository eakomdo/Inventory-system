#Build a basic inventory system for a small shop using Python. It will allow users to:

# View all items

# Add a new item

# Update item stock

# Delete an item

#  ** Calculate total stock value



Inventory = {
    "items_1": {
        "name": "Google Pixel 10",
        "stock": 10,
        "price": 5.0
    },

    "items_2": {
        "name": "Candy",
        "stock": 20,
        "price": 3.0
    },

    "items_3": {
        "name": "Macbook Pro 2024",
        "stock": 15,
        "price": 7.5
    },

    "items_4": {
        "name": "Rolls Royce",
        "stock": 5,
        "price": 10.0
    },

    "items_5": {
        "name": "iPhone 15",
        "stock": 8,
        "price": 6.0
    }
}


#View all items
print("Current Inventory:")
print("-" * 30)

print(f"Item 1: {Inventory['items_1']['name']}")
print(f"Stock: {Inventory['items_1']['stock']}, Price: ${Inventory['items_1']['price']}")

print(f"Item 2: {Inventory['items_2']['name']}")
print(f"Stock: {Inventory['items_2']['stock']}, Price: ${Inventory['items_2']['price']}")

print(f"Item 3: {Inventory['items_3']['name']}")
print(f"Stock: {Inventory['items_3']['stock']}, Price: ${Inventory['items_3']['price']}")

print(f"Item 4: {Inventory['items_4']['name']}")
print(f"Stock: {Inventory['items_4']['stock']}, Price: ${Inventory['items_4']['price']}")

print(f"Item 5: {Inventory['items_5']['name']}")
print(f"Stock: {Inventory['items_5']['stock']}, Price: ${Inventory['items_5']['price']}")


# Add a new item
Inventory.update({
    "items_6": {
        "name": "Samsung Galaxy S23",
        "stock": 12,
        "price": 4.5
    }
})

# Assign the updated inventory to a new variable
Updated_Inventory = Inventory

print(f"\nNew item added is items_6: {Inventory['items_6']['name']}")
print(f"Stock: {Inventory['items_6']['stock']}, Price: ${Inventory['items_6']['price']}")


# Update item stock

Inventory['items_5']['stock'] += 5  # Add 5 to current stock
print(f"\nUpdated stock for items_5: {Inventory['items_5']['name']}")