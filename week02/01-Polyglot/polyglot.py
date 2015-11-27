import sqlite3
from subprocess import call
import sys


def parse_command(command):
    return tuple(command.split(" "))


def is_command(command_tuple, command_string):
    return command_tuple[0] == command_string


def fetch_languages(conn):
    cursor = conn.cursor()
    query = "SELECT id, language, guide, answered FROM languages"
    result = []

    for row in cursor.execute(query):
        result.append(row)

    return result


def create_language_folder(language):
    call("mkdir {}".format(language), shell=True)


def create_language_source(language, filename, source):
    file = open(language + "/" + filename, "w")
    file.write(source)
    file.close()


def create_menu():
    menu = ["Hello and Welcome!",
            "I am the compiler.",
            "You can ask me to output different source files.",
            "I will provide guides for compiling too."
            "When you are ready, you can provide me with the answer \
from the code.",
            "And I will reveal a secret to you!",
            "Type help, to get you started."]

    return "\n".join(menu)


def create_help():
    help = ["Here is the list of commands:",
            "",
            "list - This will list all available languages",
            "start <n> - This will start you with the language #n",
            "answer <n> <answer> - This will check your answer for language n",
            "",
            "Your objective is to get all answers right!",
            "But first, you have to finish the code for the compiler,",
            "since it is not complete!"]

    return "\n".join(help)


def get_language_answered_state(answered):
    if answered == 0:
        return "NOT_DONE"

    return "DONE"


# should consider database
def create_language_list(conn):
    languages = fetch_languages(conn)
    pattern = "{} [{}] - {}"
    l = lambda x: pattern.format(get_language_answered_state(x[3]), x[0], x[1])
    languages = map(l, languages)

    return "\n".join(languages)


def open_connection(database):
    conn = sqlite3.connect(database)
    return conn


def trigger_start(conn, command):
    cursor = conn.cursor()
    lang_id = int(command[1])
    query_lang = "SELECT language, guide, answered FROM languages WHERE id = ?"
    result_lang = cursor.execute(query_lang, (lang_id, )).fetchone()

    if get_language_answered_state(result_lang[2]) == "DONE":
        print("Hey, you have DONE this. Go get another language!")
        return

    query_sources = "SELECT file_name, source FROM sources WHERE lang_id = ?"
    result_source = cursor.execute(query_sources, (lang_id, ))

    create_language_folder(result_lang[0])

    for source_row in result_source:
        create_language_source(result_lang[0], source_row[0], source_row[1])

    print("You have made a choice!")
    print(result_lang[1])
    sys.exit(0)


def trigger_unknown_command():
    unknown_command = ["Error: Unknown command!",
                       "Why don't you type help,",
                       "to see a list of commands."]

    return "\n".join(unknown_command)


def check_answer(conn, lang_id, answer):
    query = "SELECT COUNT(id) FROM languages WHERE id = ? AND answer = ?"
    cursor = conn.cursor()

    result = cursor.execute(query, (lang_id, answer)).fetchone()

    return result[0] == 1


def complete_answer(conn, lang_id):
    query = "UPDATE languages SET answered = 1 WHERE id = ?"
    conn.cursor().execute(query, (lang_id,))
    conn.commit()


def trigger_answer(conn, command):
    lang_id = int(command[1])
    answer = command[2]

    if len(command) > 3:
        partial_answer = []
        for i in range(2, len(command)):
            partial_answer.append(command[i])
        answer = " ".join(partial_answer)

    print("Your answer is: {}".format(answer))

    if check_answer(conn, lang_id, answer):
        complete_answer(conn, lang_id)
        print("You got that right! Bravo!")
        print("Now, on to the next one!")
    else:
        print("Noope. This is not the right answer. Try again.")


def main():
    conn = open_connection("polyglot.db")

    print(create_menu())

    while True:
        command = parse_command(input("Enter command>"))

        if is_command(command, "help"):
            print(create_help())
        elif is_command(command, "list"):
            print(create_language_list(conn))
        elif is_command(command, "start"):
            trigger_start(conn, command)
        elif is_command(command, "answer"):
            trigger_answer(conn, command)
        elif is_command(command, "finish"):
            break
        else:
            print(trigger_unknown_command())

    conn.close()

if __name__ == '__main__':
    main()
