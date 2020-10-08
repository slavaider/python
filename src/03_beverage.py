class Beverage:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        sum_result = [prices[i] for i in self.ingredients]
        return f'${sum(sum_result):1.2f}'

    def get_price(self):
        sum_result = [prices[i] for i in self.ingredients]
        return f'${sum(sum_result) * 2.5:1.2f}'

    def get_name(self):
        temp = sorted([i.replace("ies", "y") for i in self.ingredients])
        return f"{' '.join(temp)} {'Fusion' if len(temp) > 1 else 'Smoothie'}"


if __name__ == '__main__':
    # Стоимость 'напитков'
    prices = {"Strawberries": 1.50, "Banana": 0.50, "Mango": 2.50,
              "Blueberries": 1.00, "Raspberries": 1.00, "Apple": 1.75,
              "Pineapple": 3.50}
    b = Beverage(["Strawberries", "Banana", "Mango", "Blueberries"])
    b1 = Beverage(["Banana"])
    print(b1.get_price())
    print(b.get_name())
    print(b1.get_name())
