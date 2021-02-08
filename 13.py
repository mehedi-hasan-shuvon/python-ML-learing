#........object oriented programming...........

class Employee:
    __name=None  # here __ means its private
    __id=0
    __salary=0

    #constructor
    def __init__(self,name,id,salary):
        self.__name=name
        self.__id=id
        self.__salary=salary
        
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
        

harry =Employee()
harry.set_name('harry')
print(harry.get_name())

mehedi=Employee('mehedi',11707144,400000000)

print(mehedi.get_name())
