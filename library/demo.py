"""A demo class that has some primitive debug stuff at the end of it"""

class Demo(object):
    'Has a name which you can get or change and must be set when you create the object'

    def __init__(self, name):
        'The constructor method.  Runs when you create the object'
        self.name = name

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name

if __name__ == "__main__":
    'If this file is run on its own the following code runs'

    def debug():
        mydemo = Demo('hello world')
        print('Object created')
        print('Name property is ', mydemo.getname())
        mydemo.setname(input('changing name, what would you lie it to be?'))
        print('Name property is ', mydemo.getname())

    debug()