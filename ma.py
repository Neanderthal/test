# -*- coding: utf-8 -*-

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class Parent(object):
    def isFirst(self):
        raise NotImplementedError
    
    @property
    def isSecond(self):
        return not self.isFirst()
        
    @isSecond.setter
    def isSecond(self, value):
        raise AttributeError('isSecond is not accepted values')
      

class First(Parent):
    def isFirst(self):
        return True
    


class Second(Parent):
    def isFirst(self):
        return False

    
class A(First):
    def __init__(self):
        self.i = 3

    def fnc(self,a1):
        if a1 == 7:
            raise MyError("Error text")
        return 6 * a1

    