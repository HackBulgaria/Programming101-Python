class Panda:
    pass


def create_panda(attributes):
    panda = Panda()

    for key, value in attributes.items():
        setattr(panda, key, value)

    return panda

p = create_panda({'name': 'Ivo', 'age': 23, 'weight': 80})
print(p.__dict__)
