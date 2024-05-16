#!/usr/bin/env python3
from models.person import Person

class Owner(Person):
    def __init__(self, name, age, experience=0):
        super().__init__(name, age)
        self.experience = experience

    # def get_name(self):
    #     return self._name
    
    # def set_name(self, new_name):
    #     if type(new_name) == str:
    #         self._name = new_name
    #     else:
    #         raise TypeError('Name must be of type str')
    
    # name = property(get_name, set_name)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            raise TypeError('Name must be of type str')

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise TypeError('Age must be an integer')

    age = property(get_age, set_age)
