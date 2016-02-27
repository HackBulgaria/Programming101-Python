import json
import xml.etree.ElementTree as ET


class ClsName:
    @property
    def clsname(self):
        return self.__class__.__name__


class Xmlable(ClsName):
    def to_xml(self):
        root = ET.Element(self.clsname)

        for key, value in self.__dict__.items():
            child = ET.SubElement(root, key)
            child.text = value

        return ET.tostring(root, encoding='unicode')

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)

        if cls.__name__ != root.tag:
            error = 'Trying to create {} from {}'.format(root.tag,
                                                         data['class_name'])
            raise ValueError(error)

        cls = globals()[root.tag]
        data = {}

        for child in root:
            data[child.tag] = child.text

        obj = cls(**data)
        return obj


class Jsonable(ClsName):
    def to_json(self, indent=4):
        data = {
            'class_name': self.clsname,
            'dict': self.__dict__
        }
        return json.dumps(data, indent=indent)

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)

        if cls.__name__ != data['class_name']:
            error = 'Trying to create {} from {}'.format(cls.__name__,
                                                         data['class_name'])
            raise ValueError(error)

        cls = globals()[data['class_name']]
        obj = cls(**data['dict'])

        return obj


class Panda(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name and self.__class__ == other.__class__


class Person(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

p = Panda(name='Ivo')

json_string = p.to_json()
xml_string = p.to_xml()

p1 = Panda.from_json(json_string)
p2 = Panda.from_xml(xml_string)

assert p == p1  # Be sure to define __eq__
assert p == p2  # Be sure to define __eq__
assert p1 == p2  # Since we are not using PHP, we are not afraid of transitivity

person = Person(name='Rado')
print(Panda.from_json(person.to_json()))  # ValueError
