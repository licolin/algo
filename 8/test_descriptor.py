# -*- encoding: utf-8 -*-
# Author: li_colin

# Descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            # cls.name = Typed(name, expected_type) or
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.nam = name
        self.shares = shares
        self.price = price

    def setName(self, val):
        self.nam = val


stock = Stock("li", 2, 3.0)
# stock.name = 1

print(stock.nam)
