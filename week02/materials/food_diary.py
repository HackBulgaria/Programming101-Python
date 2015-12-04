from datetime import datetime


class FoodDiary:

    def __init__(self):
        self._diary = {}
        self._calories = {}

    def _get_date(self):
        today = datetime.now()
        return "{}.{}.{}".format(today.day, today.month, today.year)

    def add_meal(self, meal):
        date = self._get_date()
        if date in self._diary:
            self._diary[date].append(meal)
        else:
            self._diary[date] = [meal]

        return "Ok it's done."

    def list_meal(self, date):
        if date in self._diary:
            return "\n".join(self._diary[date])
        return "No meals for that day"


class Calories:

    def __init__(self):
        self._calories = {}

    def calculate_quantity(self, amount):
        if amount.endswith("kg"):
            return int(amount[:-2])*1000

        return int(amount[:-1])

    def calculate_calories(self, meal, amount):
        return amount*int(self._calories[meal]) / 100

    def has_meal(self, meal):
        return meal in self._calories

    def add_meal_calories(self, meal, calories):
        self._calories[meal] = calories


class CLI:

    def __init__(self, diary, calories_calculator):
        self.commands = {
            "meal": diary.add_meal,
            "list": diary.list_meal
        }
        self._calories_calculator = calories_calculator

    def _create_hello_message(self):
        return "Hello"

    def _create_menu_message(self):
        return "Help text"

    def _create_calories_for_meal(self, meal):
        return "I don't have {} in the calories database.".format(meal)

    def _create_meal_and_calories_message(self, calories):
        return "OK, this is a total of {} calories for this meal.".format(calories)

    def start(self):
        print(self._create_hello_message())
        print(self._create_menu_message())

        while True:
            console_input = input("Enter command:> ")
            try:
                text = console_input.split()
                command = text[0]
                if command == "exit":
                    break
                parameter = text[1]
                if command == "meal":
                    quantity = input("How much have you eaten?> ")
                    if not (quantity.endswith("kg") or quantity.endswith("g")):
                        raise Exception
                    quantity = self._calories_calculator.calculate_quantity(quantity)
                    if not self._calories_calculator.has_meal(parameter):
                        print(self._create_calories_for_meal(parameter))
                        calories_for_meal = input("How much calories per 100g?> ")
                        self._calories_calculator.add_meal_calories(parameter, calories_for_meal)
                    calories = self._calories_calculator.calculate_calories(parameter, quantity)
                    print(self._create_meal_and_calories_message(calories))
                    print(self.commands[command](parameter))
                else:
                    print(self.commands[command](parameter))
            except:
                print("You entered invalid command. Please check the help menu for more information.")


def main():
    diary = FoodDiary()
    calories_calculator = Calories()
    interface = CLI(diary, calories_calculator)
    interface.start()

if __name__ == '__main__':
    main()
