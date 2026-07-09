import json

class Product:

    def load_products(self):
        """Load inventory from disk.

        Returns an empty list if the file is missing, empty, or contains invalid JSON.
        """
        filepath = "inventory.json"
        try:
            with open(filepath, "r") as f:
                raw = f.read().strip()
                if not raw:
                    return []
                return json.loads(raw)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []


    def low_stock_report(self, products, threshold = 5):
        low_quantity_product = []
        for product in products:
            if product["Quantity"] < threshold:
                low_quantity_product.append(product)
        return low_quantity_product
        

    def save_product(self, filepath, product):
        with open(filepath, "w") as f:
            json.dump(product, f, indent=2)
            
            

    def add_product(self, id,name, price, quantity):
        product = {
            "Id": id,
            "Name": name,
            "Price": float(price),
            "Quantity": int(quantity)
        }

        products = self.load_products()

        if products:
            
            for p in products:
                if product["Id"] == p["Id"]:
                    return f" iD {product['Id'] } already exist "
            products.append(product)
            self.save_product("inventory.json", products)
            print(f"product {product['Name']}  added succesfull ")


        else:
            products.append(product)
            self.save_product("inventory.json", products)
            print(f"product {product['Name']}  added succesfull ")
            
    def remove_product(self, id, quantity):
        products = self.load_products()
        quantity = int(quantity)
        for product in products:
            if product["Id"] == id:
                if product["Quantity"] >= quantity:
                    product["Quantity"] -= quantity
                    self.save_product("inventory.json", products)
                    print(f"product {product['Name']}  sold succesfull, {product['Quantity']} left ")
                else:
                    return f" only {product["Quantity"]} left "
            else:
                low_product = self.low_stock_report(products)
                if low_product:
                    print("Low product identify, check the low stock report for more information")
                    self.save_product("low_stock_report.json", low_product)
                
        return None



    
    
    def upgrade_quantity(self, id, quantity):
        products = self.load_products()
        quantity = int(quantity)
        for product in products:
            if product["Id"] == id:
                product["Quantity"] += quantity
            else:
                return f" Product with ID {id} not found "
        
        self.save_product("inventory.json", products)

def input_handling(choice):
    data = []
    formText = ["Id", "Quantity", "Name", "Price"]
    if int(choice) in [2, 3]:
        print("Enter line by line the following information")
        for i in range(2):
            input_value = input(f'{formText[i]}:   ')
            data.append(input_value)
    elif int(choice) in [1]:
        print("Enter line by line the following information")
        for i in range(4):
            input_value = input(f'{formText[i]}:   ')
            data.append(input_value)
    return data

def display_menu():
    print("1 - add product")
    print("2 - upgrade quantity product")
    print("3 - remove a product")
    print("4 - List all products")
    print("q - exit")

def main():
    
    print(f" {"==" * 2 } Inventory manager {"==" * 2} ")
    display_menu()
    inventory = Product()
    while True:
        choice = input(' ')
        if choice == "1":
            data = input_handling(choice)
            inventory.add_product(data[0], data[2], data[3], data[1])
            display_menu()
        elif choice == "2":
            data = input_handling(choice)
            inventory.upgrade_quantity(data[0], data[1])
            display_menu()
        elif choice == "3":
            data = input_handling(choice)
            print(data)
            inventory.remove_product(data[0], data[1])
            display_menu()
        elif choice == "4":
            print(inventory.load_products())
            display_menu()
        elif choice == "q":
            print("Thanks for using!!!")
            break
        else:
            display_menu()


if __name__ == "__main__":
    main()