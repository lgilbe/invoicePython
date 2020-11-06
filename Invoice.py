class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_Impure_Price = 0
        for x, y in products.items():
            total_Impure_Price += float(y['unit_price']) * int(y['qnt'])
        total_Impure_Price = round(total_Impure_Price, 2)
        return total_Impure_Price

    def totalDiscount(self, products):
        total_discount = 0
        for x, y in products.items():
            total_discount += (int(y['qnt']) * float(y['unit_price'])) * float(y['discount']) / 100
        total_discount = round(total_discount, 2)
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput
