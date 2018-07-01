"""Proceesss errors sent to it, like if you cannot connect"""

class Problem(object):
    'Takes a problem message and processes it somehow, like logging the problem, notifying or throwing a diaglog box'

    def __init__(self, probmsg):
        self.msg = probmsg

    def report(self):
        print(self.msg)
