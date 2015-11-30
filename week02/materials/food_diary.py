from datetime import datetime


class FoodDiary:

    def __init__(self):
        self._json = {}

    def _get_date(self):
        today = datetime.now()
        return "{}.{}.{}".format(today.day, today.month, today.year)

    def add_meal(self, meal):
        date = self._get_date()
        if date in self._json:
            self._json[date].append(meal)
        else:
            self._json[date] = [meal]

        return "Ok it's done."

    def list_meal(self, date):
        if date in self._json:
            return "\n".join(self._json[date])
        return "No meals for that day"


class CLI:

    def __init__(self, obj):
        self.commands = {
            "meal": obj.add_meal,
            "list": obj.list_meal
        }

    def _create_hello_message(self):
        return "Hello"

    def _create_menu_message(self):
        return "Help text"

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
            except:
                print("Command as first and parameter as second argument are expected")
            print(self.commands[command](parameter))


def main():
    diary = FoodDiary()
    interface = CLI(diary)
    interface.start()

if __name__ == '__main__':
    main()
