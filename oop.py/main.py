'''from turtle import Turtle, Screen
timmy=Turtle()
timmy.shape("turtle")
my_screen=Screen()
timmy.speed(1)
timmy.forward(100)
timmy.right(90)
timmy.pencolor("blue")
timmy.pensize(3)
my_screen.exitonclick()
from prettytable import PrettyTable
table=PrettyTable()
print(table)
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="l"
print(table)'''
class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,  # in ml
            "milk": 200,   # in ml
            "coffee_beans": 100,  # in grams
            "money": 0
        }
        self.prices = {
            "espresso": 1.50,
            "latte": 2.50,
            "cappuccino": 3.00
        }

    def display_resources(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee Beans: {self.resources['coffee_beans']}g")
        print(f"Money: ${self.resources['money']}")

    def check_resources(self, coffee_type):
        requirements = {
            "espresso": {"water": 50, "coffee_beans": 18},
            "latte": {"water": 200, "milk": 150, "coffee_beans": 24},
            "cappuccino": {"water": 250, "milk": 100, "coffee_beans": 24}
        }
        for item, amount in requirements[coffee_type].items():
            if self.resources[item] < amount:
                return False
        return True

    def process_payment(self, coffee_type):
        price = self.prices[coffee_type]
        print(f"The price of {coffee_type} is ${price}. Please insert money.")
        inserted_money = float(input("Insert money: $"))
        
        if inserted_money < price:
            print("Sorry, not enough money. Money refunded.")
            return False
        elif inserted_money > price:
            change = round(inserted_money - price, 2)
            print(f"Here is your change: ${change}")
        
        self.resources["money"] += price
        return True

    def make_coffee(self, coffee_type):
        if not self.check_resources(coffee_type):
            print("Sorry, not enough resources to make that coffee.")
            return
        if not self.process_payment(coffee_type):
            return

        requirements = {
            "espresso": {"water": 50, "coffee_beans": 18},
            "latte": {"water": 200, "milk": 150, "coffee_beans": 24},
            "cappuccino": {"water": 250, "milk": 100, "coffee_beans": 24}
        }
        for item, amount in requirements[coffee_type].items():
            self.resources[item] -= amount

        print(f"Enjoy your {coffee_type}!")

    def refill_resources(self):
        self.resources.update({"water": 300, "milk": 200, "coffee_beans": 100})
        print("Resources refilled!")

    def run(self):
        while True:
            print("\nAvailable options:")
            print("1. Espresso ($1.50)")
            print("2. Latte ($2.50)")
            print("3. Cappuccino ($3.00)")
            print("4. Check resources")
            print("5. Refill resources")
            print("6. Exit")

            choice = input("What would you like to do? (Enter 1/2/3/4/5/6): ")

            if choice == '1':
                self.make_coffee("espresso")
            elif choice == '2':
                self.make_coffee("latte")
            elif choice == '3':
                self.make_coffee("cappuccino")
            elif choice == '4':
                self.display_resources()
            elif choice == '5':
                self.refill_resources()
            elif choice == '6':
                print("Thank you for using the coffee machine. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

#if __name__ == "__main__":
coffee_machine = CoffeeMachine()
coffee_machine.run()

