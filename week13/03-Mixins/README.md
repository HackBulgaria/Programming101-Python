# Mixins

## Serializers/Deserializers to and from JSON / XML

In a python module `utils.serializers`, create the following classes:

* `Jsonable` with methods
  * `to_json(indent=4)`
  * classmethod `from_json(json_string)`
* `Xmlable` with methods:
  * `to_xml()`
  * classmethod `from_xml(xml_string)`

Those classes should serve as mixins. Here is example usage:


```python
class Panda(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name
```

Now, lets see how we can turn our pandas in JSON / XML:

```python
>>> p = Panda(name='Ivo')
>>> p.to_json()
{
    "dict": {
        "name": "Ivo"
    },
    "class_name": "Panda"
}
>>> p.to_xml()
<Panda><name>Ivo</name></Panda>
```

Now, the other way around - we should be able to create panda instances from their respective JSON / XML representations:

```python
p = Panda(name='Ivo')
json_string = p.to_json()
xml_string = p.to_xml()

p1 = Panda.from_json(json_string)
p2 = Panda.from_xml(xml_string)

assert p == p1 #  Be sure to define __eq__
assert p == p2 #  Be sure to define __eq__
assert p1 == p2 #  Since we are not using PHP, we are not afraid of transitivity
```

Make additional type checks. Since we are keeping the `class_name` in our JSON or XML representation, if you try to create `Panda` from `Person` representation, raise a `ValueError`:

```python
class Person(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
    
person = Person(name='Rado')
print(Panda.from_json(person.to_json()))  # ValueError
```

### Hints

* For XML, use the standard library - <https://docs.python.org/3/library/xml.etree.elementtree.html>
* think of `globals()` and `locals()`

## Enumerable

Implement a basic class `Collection`, which does the following:

* Takes a variable number or arguments in its contructor - `Collection(1, 2, 3)`
* Implements the **iterator pattern**.
* Implements equality - `Collection(1) == Collection(1)`

In our Collection, we are going to mixin some classes - `Enumerable` and `Exensible`

Finish the following code, implementing some of the methods of our `Enumerable` mixin:

```python
class Enumerable:
    def take(self, n):
        pass

    def drop(self, n):
        pass

    def take_while(self, predicate):
        pass

    def drop_while(self, predicate):
        pass

    def map(self, callable):
        pass

    def filter(self, predicate):
        pass

    def reduce(self, start_value, operator):
        pass

    # Returns True, if value is in self
    def search(self, value):
        pass
```

Example usage:

```python
class Collection(Enumerable, Extensible):
    pass


c = Collection(1, 2, 3)

assert c == c.map(lambda x: x)
assert Collection(2) == c.filter(lambda x: x % 2 == 0)
assert 6 == c.reduce(0, lambda x, y: x + y)
assert Collection(1, 2) == c.take(2)
assert Collection(3) == c.drop(2)
assert Collection(0, 0, 0) == Collection(0, 0, 0, 1).take_while(lambda x: x == 0)
assert Collection(1) == Collection(0, 0, 0, 1).drop_while(lambda x: x == 0)
assert Collection(1).search(1)
```

The `Extensible` mixing should implement a method, that will react to the `+` operator.

It should return a new **whatever collection that mixes in `Extensible`** with the concatenation.

Example:

```python
c = Collection(1, 2, 3)
c1 = c + [1, 2, 3]

assert c1 == Collection(1, 2, 3, 1, 2, 3)
```

