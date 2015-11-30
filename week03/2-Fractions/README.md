# An Immutable Fraction class

We want to create a simple fraction class:

```python
class Fraction:
  
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)


    def __repr__(self):
        return self.__str__()
```

Our fractions should be able to do the following operations:

* `+`
* `-`
* `*`
* `==`

Implement the needed **dunder** methods in order to achieve that.

**Each operation that mutates the fraction, like `+`, `-` and `*` should return a new `Fraction`!**

Examples:

```python
a = Fraction(1, 2)
b = Fraction(2, 4)

a == b # True

a + b # 1
a - b # 0
a * b # 1 / 4
```

