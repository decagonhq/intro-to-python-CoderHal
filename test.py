class MyClass:
    AGE = 5
    
    @classMethod
    def get_computed_age(cls, add = 3):
        return MyClass.AGE + add