from prettytable import PrettyTable
import sqlite3
import settings


class DBCommunicator:

    def __init__(self, cursor):
        self.cursor = cursor

    def get_movies(self):
        return self.cursor.execute('''SELECT id, movie_name, movie_rating
                                      FROM Movies
                                      ORDER BY movie_rating DESC''')

    def get_projections(self, movie_id):
        return self.cursor.execute('''SELECT Projections.id, projection_type, projection_time,
                                             projection_date, movie_id, movie_name
                                      FROM Projections
                                      JOIN Movies
                                      ON Projections.movie_id = Movies.id
                                      WHERE movie_id = ?
                                      ORDER BY projection_date''', (str(movie_id), ))

    def get_projections_with_date(self, movie_id, date):
        return self.cursor.execute('''SELECT Projections.id, projection_type, projection_time,
                                             projection_date, movie_id, movie_name
                                      FROM Projections
                                      JOIN Movies
                                      ON Projections.movie_id = Movies.id
                                      WHERE movie_id = ? AND projection_date = ?
                                      ORDER BY projection_date''', (str(movie_id), str(date)))

    def get_revervations_for_projection(self, projection_id):
        return self.cursor.execute('''SELECT row, col
                                      FROM Reservations
                                      WHERE projection_id = ?''', (projection_id, ))


class Controller:

    def __init__(self, db_communicator):
        self.db_communicator = db_communicator

    def generate_movies_table(self):
        table = PrettyTable(["id", "movie_name", "movie_rating"])
        for row in self.db_communicator.get_movies():
            table.add_row([row["id"], row["movie_name"], row["movie_rating"]])

        return table

    def create_cinema(self, projection_id):
        rows = settings.CINEMA_ROWS
        cols = settings.CINEMA_COLS
        db_data = self.db_communicator.get_revervations_for_projection(projection_id)
        cinema = []

        row_headers = [" " if x == 0 else x for x in range(rows + 1)]
        cinema.append(row_headers)

        for row in range(rows):
            cinema.append([str(row + 1) if col == 0 else "." for col in range(cols+1)])

        for row in db_data:
            cinema[row["row"]][row["col"]] = "X"

        return cinema

    def generate_projections_table(self, movie_id, date):
        if date is not None:
            db_result = self.db_communicator.get_projections_with_date(movie_id, date)
        else:
            db_result = self.db_communicator.get_projections(movie_id)

        table = PrettyTable(["projection_id", "projection_type", "projection_time",
                             "projection_date", "movie_id", "movie_name"])

        for row in db_result:
            table.add_row([row["id"], row["projection_type"], row["projection_time"],
                           row["projection_date"], row["movie_id"],
                           row["movie_name"]])

        return table

    def generate_reservations_table(self, data):
        table = PrettyTable(data[0])
        for row in data[1:]:
            table.add_row(row)

        return table


class CLI:

    def __init__(self, controller):
        self.controller = controller

        self.__user_is_active = True
        self.commands = {
            "show_movies": self.show_movies,
            "show_projections": self.show_projections,
            "make_reservations": self.make_reservations,
            "exit": self.exit
        }

    def show_movies(self, *args):
        print(self.controller.generate_movies_table())

    def show_projections(self, *args):
        movie_id = args[0]
        date = None
        if len(args) > 1:
            date = args[1]

        print(self.controller.generate_projections_table(movie_id, date))

    def show_reservations(self, data):
        print(self.controller.generate_reservations_table(data))

    def make_reservations(self, *args):
        username = input("Enter your name: ")
        number_of_tickets = int(input("Enter number of tickets: "))
        self.show_movies()
        movie_id = int(input("Enter movie id: "))
        self.show_projections(movie_id)
        projection_id = int(input("Enter projection id: "))
        self.show_reservations(self.controller.create_cinema(projection_id))
        # ask for ticket seats
        # if finalize 
            # insert query

    def exit(self, *args):
        self.__user_is_active = False

    def start(self):
        print("Hello!")
        while self.__user_is_active:
            command = ""
            parameter1 = None
            parameter2 = None

            user_input = input("Enter command: ")
            user_input = user_input.split()
            command = user_input[0]
            if len(user_input) > 1:
                parameter1 = user_input[1]
                if len(user_input) > 2:
                    parameter2 = user_input[2]

            self.commands[command](parameter1, parameter2)


class Validator:
    def __init__(self):
        pass

    def validate_ticket(self):
        raise Exception("DA")


def main():
    db = sqlite3.connect("cinema_data.db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    db_communicator = DBCommunicator(cursor)
    controller = Controller(db_communicator)
    cli = CLI(controller)
    cli.start()


if __name__ == '__main__':
    main()
