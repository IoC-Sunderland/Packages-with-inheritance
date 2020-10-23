from sub_1.sub_1_classes import MyBaseClass

class MySubClass(MyBaseClass):

    def __init__(self):
        self.greeting = 'Hi from MySubClass'
    
    def __repr__(self):
        return self.greeting

