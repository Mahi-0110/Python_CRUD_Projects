def inventory_management_system():
    products = []
    prices = []
    while True:
        print("1. Add Product\n2. View Products\n3. Search Product\n4. Delete Product\n5. Total Inventory Value\n6. Most Expensive Product\n7. Exit")
        option = int(input("Enter option here:"))
        #add products
        if option == 1:
            product = input("Enter Product:")
            price = int(input("Enter price:"))
            products.append(product)
            prices.append(price)
            print("product added successfully!")
        #view product
        elif option ==2:
            if len(products) == 0:
                print("No product is added")
            else:
                for view in range (len(products)):
                    print(f"{products[view]}->{prices[view]}")
        #search product
        elif option == 3:
            search_product =input("Enter product:")
            if search_product in products:
                print("Product Found")
            else:
                print("product is not found")
        #delete product
        elif option == 4:
            delete_product=input("enter product:")
            if delete_product in products:
                index_delete = products.index(delete_product)
                products.pop(index_delete)
                prices.pop(index_delete)
                print("Product deleted successfully")
            else:
                print("No product is founded")
        #Total inventory value
        elif option == 5:
            total = 0
            for i in prices:
                total = total + i
            print(f"Total inventory value:{total}")
        #Most expensive product
        elif option == 6:
            high =0
            for expensive in prices:
                if expensive>high:
                    high = expensive
            index = prices.index(expensive)
            print(f"{products[index]}->{prices[index]}")
        #exit
        elif option == 7:
            break
        else:
            print("Invalid option")
inventory_management_system()

