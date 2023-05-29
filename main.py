import products
import store


def start(store_obj):
    """Show options to user and run selected function"""
    while True:
        print("Menu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("All products in store:")
            all_products = store_obj.get_all_products()
            for i, product in enumerate(all_products, 1):
                print(f"{i}. {product.show()}")
            print()

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_quantity}\n")

        elif choice == "3":
            item_number = input("Enter the item number for the order: ")
            try:
                item_number = int(item_number)
                selected_product = store_obj.get_all_products()[
                    item_number - 1]
                quantity = int(input("Enter the quantity: "))
                try:
                    order_price = store_obj.order(
                        [(selected_product, quantity)])
                    print(f"Order cost: {order_price} dollars.\n")
                except ValueError as error:
                    print(f"Order failed: {str(error)}\n")
            except (ValueError, IndexError):
                print("Invalid item number.\n")

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.\n")


def main():
    """Setup initial stock of inventory"""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity_limit=250)
        ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
