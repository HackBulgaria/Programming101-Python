import inspect

TYPES = {
    int: 'INTEGER',
    str: 'VARCHAR'
}


def map_python_to_sql(py_type):
    if py_type not in TYPES:
        return TYPES[str]

    return TYPES[py_type]


def varchar():
    return str


def integer():
    return int


def pluralize(string):
    plural_forms = ['s', 'es']

    for form in plural_forms:
        if string.endswith(form):
            return string

    # FIXME: Not a proper english
    return string + 's'


def extract_dict_from_class(cls):
    members = [m for m in inspect.getmembers(cls)
               if '__' not in m[0]]
    attributes = {m[0]: m[1] for m in members}
    return (cls.__name__, attributes)


def class_to_table(name, attributes):
    create_sql = """
        CREATE TABLE {name}(
            id INTEGER PRIMARY KEY AUTO INCRAMENT,
            {columns}
        );

    """
    data = {
      "name": pluralize(name),
      "columns": ""
    }

    columns = []
    for attr in attributes:
        value_type = attributes[attr]
        columns.append("{} {}".format(attr,
                                      map_python_to_sql(value_type)))

    data['columns'] = ",\n".join(columns)
    return create_sql.format(**data)


class Person:
    email = varchar()
    password = varchar()
    age = integer()

print(class_to_table(*extract_dict_from_class(Person)))
