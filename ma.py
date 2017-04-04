# -*- coding: utf-8 -*-

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class Parent(object):
    def isFirst(self):
        return 1
    
    @property
    def isSecond(self):
        return 0
        
    @isSecond.setter
    def isSecond(self, value):
        raise AttributeError('isSecond')
      

class First(Parent):
    def isFirst(self):
        return 1
    
    @property
    def isSecond(self):
        return 0
        


class Second(Parent):
    def isFirst(self):
        return 0

    @property
    def isSecond(self):
        return 1
    
    
class A(First):
    def __init__(self):
        self.i = 3

    def fnc(self,a1):
        if a1 == 7:
            raise MyError("Error text")
        return 6 * a1

    