class MyClass:
    class_var = "The class variable"
  
    def __init__(self, instance_var):
        self.instance_var = instance_var
    
    def display(self):
        print("This is class variable: " + MyClass.class_var)
        print("This is instance variable: " + self.instance_var)
        
    def instance_method(self):
        """
        Instance Methods: The first methodmethod is an instance method. 
        The parameter selfpoints to an instance of MyClass. 
        It can also access the class itself through self.__class__ property.
        """
        return 'instance method called', self
    
    
    @classmethod
    def class_method(cls, x):
        """
        class method. It takes a cls parameter that points to the class, 
        and can only modify class states.
        These are methods that are bound to the class and not the instance of the class.
        """
        print(f"Class method called with {x}")
        print(f"Accessing class variable: {cls.class_var}")
        
    @staticmethod
    def add(x, y):
        """
        static method. It does not take the mandatory self nor a 
        cls parameter. As a result, it can’t access class or instance state
       does not have access to the instance or class variables.
        """
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y
    


class Mycar:
    def __init__(self, brand=None):
        self._brand = brand
        
    # getter
    def get_brand(self):
        print("Getting brand")
        return self._brand

    # setter
    def set_brand(self, value):
        self._brand = value
        print("Setting brand", self._brand)   
        

var = MyClass("The instance variable")
var.display()

a= var.instance_method()
print(a)


benz = Mycar()
benz.set_brand("lexus")
brand = benz.get_brand()
print(brand)


# @prperty = This decorator is used to define a property, which allows you to access a method like an attribute.

class Mycar_second:
    def __init__(self, brand=None):
        self._brand = brand
    
    @property
    def brand(self):
        print("Getting brand")
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value
        print("Setting brand", self._brand)
        
    @brand.deleter
    def brand(self):
        print("Deleting brand", self._brand)
        del self._brand
        
benz = Mycar_second()
benz.brand = "benz" 
benz.brand