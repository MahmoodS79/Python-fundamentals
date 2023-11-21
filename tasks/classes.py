'''
# Mutability
class name:
    stat_attr = 0
    def pr(self):
        print(self.__class__.__name__)

n = name()
n.stat_attr += 1
print(n.stat_attr)
print(name.stat_attr)
print(n.pr())

'''

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def area(self):
        raise NotImplementedError

class rect(Shape):
    def __init__(self):
        self.name = 'square'
        super().__init__(self.name)

    def area(self):
        return 2*2


r = rect()
print(r.area(),r.name)

def func5():
    x=5
    def func4():
        nonlocal x
        return x
    return func4()

print(dir(func5))


class Mammal():

    def __init__(self, name):
        print(name, "Is a mammal")


class canFly(Mammal):

    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)


class canSwim(Mammal):

    def __init__(self, canSwim_name):
        print(canSwim_name, "cannot swim")

        super().__init__(canSwim_name)


class Animal(canFly, canSwim):

    def __init__(self, name):
        super().__init__(name)


# Driver Code
Carol = Animal("Dog")