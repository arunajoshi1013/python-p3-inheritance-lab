#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.knowledge = []
    def learn(self, learn):
        self.knowledge.append(learn)