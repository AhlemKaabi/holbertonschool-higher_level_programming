#!usr/bin/python3
'''module documentation
'''


class Student:
    '''class Student
    '''

    def __init__(self, first_name, last_name, age):
        '''class
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''class2
        '''
        return self.__dict__
