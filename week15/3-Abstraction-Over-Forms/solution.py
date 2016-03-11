from collections import OrderedDict
from abc import ABCMeta, abstractmethod
import unittest


class ValidationError(Exception):
    pass


class BaseField(metaclass=ABCMeta):
    def __init__(self, value=None):
        self.value = value

    def is_valid(self):
        return True

    @abstractmethod
    def __str__(self):
        pass


class Input(BaseField):
    def __str__(self):
        args = ['type="{}"'.format(self.__class__.type)]

        if self.value is not None:
            args.append('value="{}"'.format(self.value))

        return '<input {} />'.format(' '.join(args))


class TextInput(Input):
    type = 'text'


class SubmitInput(Input):
    type = 'submit'


class PasswordInput(Input):
    type = 'password'


class EmailInput(Input):
    type = 'email'

    def is_valid(self):
        if self.value == 'ivaylo@hackbulgaria.com':
            raise ValidationError('No Pandas Allowed')


class OrderedClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result


class Form(metaclass=OrderedClass):
    def __init__(self, form_data=None):
        self.__dict__ = OrderedDict()
        self._form_data = form_data or {}

        cls_dict = vars(self.__class__)

        for key in self.__class__.members:
            if '__' not in key:
                value = cls_dict[key]

                if not callable(value):
                    self.__dict__[key] = value
                    # setattr(self, key, value)

        for key, value in self._form_data.items():
            if key in self.__dict__:
                self.__dict__[key].value = value

    @property
    def fields(self):
        return [(name, field) for name, field
                in self.__dict__.items()
                if not name.startswith('_')]

    def is_valid(self):
        for _, field in self.fields:
            field.is_valid()

        cls_dict = vars(self.__class__)

        for name, field in self.fields:
            validator_name = 'validate_{}'.format(name)
            validator = cls_dict.get(validator_name, False)

            if validator and callable(validator):
                getattr(self, validator_name)(field)

    def __str__(self):
        tags = ['<form>']
        tags += [str(field) for _, field in self.fields]

        tags.append(str(SubmitInput('Go!')))
        tags.append('</form>')
        return "\n".join(tags)


class LoginForm(Form):
    email = EmailInput()
    password = PasswordInput()

    def validate_password(self, pwd_field):
        print('I cant believe this works')
        print(pwd_field)

f = LoginForm({'email': 'ivaylo@hacksoft.io'})
print(f)

f.is_valid()
