class Product:
    def __init__(self, price, item_name, weight, brand, status="For Sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "sold"
        print("This item is now " + self.status)
        return self

    def addTax(self, tax):
        self.price += tax
        print("After tax, you owe: " + str(self.price))
        return self

    def returnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
            print("This item is now " + self.status)

        elif reason_for_return == "like new":
            self.status = "for sale"
            print("This item is now " + self.status)

        elif reason_for_return == "opened":
            self.status = "used"
            self.price = self.price * 0.80
            print("This item is now " + self.status + " and is "
                  "discounted to $" + str(self.price))
        return self

    def displayInfo(self):
        print("\n")
        print("Price: " + str(self.price))
        print("Item Name: " + str(self.item_name))
        print("Weight: " + str(self.weight))
        print("Brand: " + str(self.brand))
        print("Status: " + str(self.status))
        print("------" * 5)
        return self


product1 = Product(7, "Chicken", 2, "Perdue Chicken")
product1.displayInfo().sell().addTax(0.06)

product2 = Product(2, "Pop Tart", 1, "Kelloggs")
product2.displayInfo().returnItem("defective")

product3 = Product(5, "Tea", 4, "Honest Tea")
product3.displayInfo().returnItem("opened")
