#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, fname, lname, knowledge):
        super().__init__(fname, lname)
        self.knowledge = knowledge

    def teach(self):
        return self.knowledge[random.randint(0, self.knowledge.__len__())]