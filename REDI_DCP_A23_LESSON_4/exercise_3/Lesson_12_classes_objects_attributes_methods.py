class inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, item_name, stock_count, item_price):
        if item_id not in self.inventory:
            self.inventory[item_id] = {
                "item_name" : item_name,
                "stock_count" : stock_count,
                "item_price" : item_price
            }

        else:
            print(f"Item with ID: {item_id} already exist in the inventoy.")

    def update_item(self, item_id, stock_count, item_price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
            self.inventory[item_id]["item_price"] = item_price

        else:
            print(f"Item with ID: {item_id} not found in the inventory.")
    
    def check_item_details(self, item_id):  
        if item_id in self.inventory:
            item_details = self.inventory[item_id]
            print(f"Item Name: {item_details['item_name']}")
            print(f"Stock Count: {item_details['stock_count']}")
            print(f"Item Price: ${item_details['item_price']:.2f}")

        else:
            print(f"Item with ID: {item_id} not found in the inventory.")


    def minus_item(self, item_id, quantity):
        if item_id in self.inventory:
            current_stock =self.inventory[item_id]["stock_count"]
            if current_stock >= quantity:
                self.inventory[item_id]["stock_count"] -= quantity
                print(f"Successfully deducted {quantity} items from {item_id} stock.")

            else:
                print("Not enough item in stock")

        else:
            print("Item not found in the inventory")

Inventory_System = inventory()
Inventory_System.add_item(1, "mouse A", 50, 12.99)
Inventory_System.add_item(2, "mouse B", 70, 19.99)
Inventory_System.update_item(5,10, 9.99) #prints item not in the inventory
Inventory_System.update_item(2, 100, 21.99) # update old item price to new price and overwrite the  old stock_count with the new stock_count
Inventory_System.minus_item(2, 10)
Inventory_System.check_item_details(2)
Inventory_System.check_item_details(1)
