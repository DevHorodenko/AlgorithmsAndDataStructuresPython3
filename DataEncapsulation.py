class Person():

    def __init__(self):
        self.__name = None
        pass

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

p = Person()
p.name = 'Jhon'
print(p.name)