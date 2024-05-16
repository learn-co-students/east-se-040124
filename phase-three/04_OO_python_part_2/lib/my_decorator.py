def execute_function(func):
# def execute_function(name):
    # def call_with_name(func):
    #     func(name)
    
    # return call_with_name
    func('Apollo')

def walk(pet_name):
    print(f'{pet_name} has been for a walk')

# @execute_function("apollo")
@execute_function
def feed(pet_name):
    print(f'{pet_name} has been feed')

# higher order function
# function parameter and/or return functions

