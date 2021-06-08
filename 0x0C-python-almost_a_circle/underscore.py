#!/usr/bin/puthon3
class Sample():

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3


class SecondClass(Sample):

    def __init__(self):
        super().__init__()
        self.a = "overridden"
        self._b = "overridden"
        self.__c = "overridden"



obj1 = Sample()
print(obj1._Sample__c)

obj2 = SecondClass()
print(obj2.a)
print(obj2._b)
print(obj2._SecondClass__c)
print(obj1._Sample__c)
