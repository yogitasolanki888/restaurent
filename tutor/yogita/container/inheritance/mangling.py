# name mangling in attributes
# class Car:
#     def __init__(self):
#         self.foo = 'Test One'
#         self._bar = 'Test Two'
#         self.__baz = 'Test Three'

# car = Car()
# print(car.foo)
# print(car._bar)
# print(car.__dict__)
# print(dir(car))
# print(car._Car__baz)

# another way accessing attributes  using instance method
# class Car:
#     def __init__(self):
#         self.foo = 'Test One'
#         self._bar = 'Test Two'
#         self.__baz = 'Test Three'
#     def get_baz(self):
#         return self.__baz

# car = Car()
# print(car.get_baz())


# name mangling in method (function)
class Car:
    def __init__(self):
        self.foo = "Test One"
        self._bar = "Test Two"
        self.__baz = "Test Three"

    def __Sub(self):
        return "Zoom"

    def Get(self):
        return self.__Sub()


car = Car()
# print(car.__Sub())
# print(car.Get())
print(car._Car__Sub())
