# Abstaction Over Forms

We are going to implement our own abstraction over forms. We are going to make it outside of Django - as a simple Python module.

Here is the interface that we need to have:

## BaseField

The main class that we are going to use for all forms looks like this:

```python
from abc import ABCMeta, abstractmethod


class BaseField(metaclass=ABCMeta):
    @abstractmethod
    def is_valid(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

```

We are using the [`abc`](https://docs.python.org/3.4/library/abc.html) module to make a Java-like abstract class with abstract methods.

All other Fields should subclass our `BaseField`

## Form

There should be a base `Form` class which we are going to subclass for our forms. A form is a collection of fields.

We should have a declarative way of making forms.

Here is an example usage:

```python
class Field(BaseField):
    def is_valid(self):
        return True

    def __str__(self):
        return "<input />"


class LoginForm(Form):
    name = Field()
    password = Field()
```

As simple as that.

Now, when we make an instance of our form, we should be able to access `name` and `password` as instance variables:

```python
form = LoginForm()
assert isinstance(form.name, Field)
assert isinstance(form.password, Field)
```

## String representation

* Our fields should have `__str__` which returns a **valid HTML representation of the given field**
* The base `Form` should also have a `__str__` method, which returns the **HTML representation of the entire form**

Here are the examples (the `BaseField` subclasses are up to you. This is just one way to do it)

```python
class LoginForm(Form):
    name = TextInput()
    password = PasswordInput()

f = LoginForm(action='/', method='POST')
print(str(f))
```

Should yield the following result:

```html
<form action='/', method='POST'>
  <input name='name' type='text' />
  <input name='password' type='password' />
  <input type='submit' />
</form>
```

## Loading data into our form

We should have a way to instantiate our form with data. For example:

```python
class LoginForm(Form):
    name = TextInput()
    password = PasswordInput()

form_data = {
  'name': 'Ivo',
  'password': 'azsampanda'
}
f = LoginForm(data=form_data, action='/', method='POST')
print(str(f))
```

Should yield the following result:

```html
<form action='/', method='POST'>
  <input name='name' type='text' value='Ivo' />
  <input name='password' type='password' value='azsampanda' />
  <input type='submit' />
</form>
```

The data should reflect in the `value` property of our inputs.

## Form attributes

As kwargs, our form should accept the following attributes:

* `action`
* `method`
* `class`
* `id`

You know what to do with them.

Quick example:

```python
class MyForm(Form):
    pass

f = MyForm(method='POST', action='/panda', class='panda_form', id='panda')
print(str(f))
```

Should yield the following result:

```html
<form method='POST' action='/panda' class='panda_form' id='panda'>
</form>
```

## Field attributes

We should be able to provide  `class` and `id` to our Fields to. Think about that.

## Validation

We should be able to validate our form. Validation should happen when our form has data and `is_valid()` is called.

The validation should happen in 2 steps:

* First, all form fields are validated, according to their own validators.
* Second, all custom form validators are run on the desired fields.

If something goes wrong during a validation, raise `ValidationError`. This error is not part of standard Python errors.

### Field validation

We should have a way to enforce field validation. Each field should define it's own `is_valid()` method, which is going to be called during form validation phase.

For example, if we have an `EmailInput`, it is a good idea to have validation for it. Other good idea is `NumberInput`

If there is no specific field validation to be done, just return `True`

### Custom field validators

Our custom validators are going to be defined as methods in our form.

If we have a field with name `name` and method with name `validate_name`, this method should be call for field validation.

Here is an example:

```python
class LoginForm(Form):
    name = TextInput()
    password = PasswordInput()

    def validate_password(self, pwd_field):
        if (pwd_field.value) < 8:
            raise ValidationError('Password length should be >= 8')
```

Now, if we call `is_valid`, after all field validation, we should call `validate_password` and pass `password` field to it.
