# -*- coding: utf-8 -*-

from ma import Second


class B(Second):
    def __init__(self, b1):
        self.tempfive = b1

    def fnc(self,b1,b2):
        return b1 * b2 * self.tempfive
